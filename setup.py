from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='choto',
    version='1.0.2',
    py_modules=['choto'],
    author='Ayush Subedi',
    author_email='ayush.subedi@gmail.com',
    description='A CLI tool that summarizes news and articles.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ayushsubedi/choto',
    python_requires='>=3.6, <3.9',
    install_requires=[
        'Click',
        'requests',
        'newspaper3k',
        'numpy==1.19.5',
        'gensim',
        'spacy==2.2.0',
        'summarizer'
    ],
    entry_points='''
        [console_scripts]
        choto=choto:cli
    ''',
    project_urls={
        'Bug Reports': 'https://github.com/ayushsubedi/choto/issues',
        'Source': 'https://github.com/ayushsubedi/choto',
    },
)
