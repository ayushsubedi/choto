import requests
import click
from newspaper import Article
from requests.exceptions import ConnectionError
from gensim.summarization import summarize
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from collections import Counter
from heapq import nlargest
from summarizer import Summarizer


try:
    nlp = spacy.load('en')
except OSError:
    from spacy.cli import download
    download('en')
    nlp = spacy.load('en')


def spacy_summary(doc, ratio):
    ''' Generate summary using spacy
    Args:
        doc: text to summarize
        ratio: ratio of the original text to summarize into
    Returns:
        summarized text using spacy
    '''
    total_sentence = len(list(doc.sents))
    summary_len = int(total_sentence * ratio)
    keyword = []
    stopwords = list(STOP_WORDS)
    pos_tag = ['PROPN', 'ADJ', 'NOUN', 'VERB']

    for token in doc:
        if(token.text in stopwords or token.text in punctuation):
            continue
        if(token.pos_ in pos_tag):
            keyword.append(token.text)
    freq_word = Counter(keyword)
    max_freq = Counter(keyword).most_common(1)[0][1]
    for word in freq_word.keys():
        freq_word[word] = (freq_word[word]/max_freq)
    sent_strength = {}
    for sent in doc.sents:
        for word in sent:
            if word.text in freq_word.keys():
                if sent in sent_strength.keys():
                    sent_strength[sent] += freq_word[word.text]
                else:
                    sent_strength[sent] = freq_word[word.text]
    summarized_sentences = nlargest(
        summary_len,
        sent_strength,
        key=sent_strength.get)

    final_sentences = [w.text for w in summarized_sentences]
    summary = ' '.join(final_sentences)
    return summary


def text_summary(algorithm, text, ratio):
    ''' Generate summary using one of the three implemented
    algorithm
    Args:
        text: text to summarize
        ratio: ratio of the original text to summarize into
    Returns:
        summarized text using input algorithm
    '''
    if (algorithm == 'gensim'):
        return summarize(text=text, ratio=ratio)
    if (algorithm == 'spacy'):
        doc = nlp(text)
        return spacy_summary(doc, ratio)
    if (algorithm == 'bert'):
        model = Summarizer()
        result = model(text, ratio)
        return ''.join(result)


@click.command()
@click.option(
    '--url',
    prompt='Enter article URL to summarize',
    help='Enter a valid URL')
@click.option(
    '--ratio',
    default=0.3,
    help='Ratio to summarize to.')
@click.option(
    '--algorithm',
    type=click.Choice(
        ['gensim', 'spacy', 'bert'],
        case_sensitive=False),
    default='gensim',
    help='Algorithm to use')
def cli(url, ratio, algorithm):
    try:
        if not url.startswith('http'):
            url = 'http://'+url
            r = requests.get(url)
            url = r.url
    except ConnectionError as ce:
        click.echo('Could not PING to the URL' + str(ce))
    else:
        article = Article(url, keep_article_html=False)
        article.download()
        article.parse()
        click.echo(text_summary(
            algorithm=algorithm,
            text=article.text,
            ratio=ratio))
