from setuptools import setup

setup(
    name='summarize',
    version='1.0',
    py_modules=['summarize'],
    author='Ayush Subedi',
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
        summarize=summarize:cli
    ''',
)
