import requests
import click
from newspaper import Article
from requests.exceptions import ConnectionError
from gensim.summarization import summarize


@click.command()
@click.option(
    '--url',
    prompt='Enter article URL to summarize',
    help='Enter a valid URL')
@click.option(
    '--words',
    default=100,
    help='Number of words to summarize to.')
def get_content(url, words):
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
        click.echo(summarize(text=article.text, word_count=words))


if __name__ == '__main__':
    get_content()
