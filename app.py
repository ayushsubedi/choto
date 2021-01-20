
import validators
import requests
import click
from newspaper import Article


def summarize(article_text, words):
    #TODO: add summarizer
    return article_text[:words]


@click.command()
@click.option('--url', default='https://abc.xyz/', help='Enter a valid URL')
@click.option('--words', default=150, help='Number of words to summarize to.')
def get_content(url, words):
    if not url.startswith('http'):
        url = 'http://'+url
        r = requests.get(url)
        url = r.url
    if (validators.url(url)):
        try:
            article = Article(url, keep_article_html=False)
            article.download()
            article.parse()
            click.echo(summarize(article.text, words))
        except Exception as e:
            click.echo(str(e))
           


if __name__ == '__main__':
    get_content()