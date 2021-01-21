from setuptools import setup

setup(
    name='term_article_summary',
    version='1.0.1',
    py_modules=['term_article_summary'],
    author='Ayush Subedi',
    author_email='ayush.subedi@gmail.com',
    description='A CLI tool that summarizes news and articles.',
    url='https://github.com/ayushsubedi/term-article-summary',
    python_requires='>=3.6, <3.9',
    install_requires=[
        'Click',
        'requests',
        'newspaper3k',
        'numpy==1.19.5',
        'gensim',
        'spacy==2.2.0',
        'en_core_web_sm @ https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.2.0/en_core_web_sm-2.2.0.tar.gz',
    ],
    entry_points='''
        [console_scripts]
        term_article_summary=term_article_summary:cli
    ''',
    project_urls={
        'Bug Reports': 'https://github.com/ayushsubedi/term-article-summary/issues',
        'Source': 'https://github.com/ayushsubedi/term-article-summary',
    },
)
