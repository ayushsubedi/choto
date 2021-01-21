import requests
import click
from newspaper import Article
from requests.exceptions import ConnectionError
from gensim.summarization import summarize


def text_summary(algorithm, text, words):
    print(algorithm)
    if (algorithm == 'gensim'):
        return summarize(text=text, word_count=words)
    # TODO: add different algorithms
    return ' '.join((text.split()[:words]))


@click.command()
@click.option(
    '--url',
    prompt='Enter article URL to summarize',
    help='Enter a valid URL')
@click.option(
    '--words',
    default=100,
    help='Number of words to summarize to.')
@click.option(
    '--algorithm',
    type=click.Choice(
        ['gensim', 'todo_other1', 'todo_other2'],
        case_sensitive=False),
    default='gensim',
    help='Algorithm to use')
def get_content(url, words, algorithm):
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
            words=words))


if __name__ == '__main__':
    get_content()
