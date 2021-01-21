import requests
import click
from newspaper import Article
from requests.exceptions import ConnectionError


def summarize(article_text, words):
    # TODO: add summarizer
    return article_text[:words]


@click.command()
@click.option(
    '--url',
    prompt='Enter article URL to summarize',
    help='Enter a valid URL')
@click.option(
    '--words',
    default=150,
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
        click.echo(summarize(article.text, words))


if __name__ == '__main__':
    get_content()
