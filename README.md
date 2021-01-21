### Term Article Summary

A CLI tool that summarizes news/articles. 

[![asciicast](https://asciinema.org/a/gTgnbAKLweXtwcefoniU96Isn.svg)](https://asciinema.org/a/gTgnbAKLweXtwcefoniU96Isn)

### Installation

#### Clone the repository

`git clone https://github.com/ayushsubedi/term-article-summary`

#### CD into the cloned directory and create a virtualenv

`python -m venv env`

### Enable virtualenv

`.\env\Scripts\activate`

### Install dependency packages from requirements.txt

`pip install -r requirements.txt`

### Run the app

`python app.py --url=https://abc.xyz --ratio=0.5 --algorithm=bert`

Usage: app.py [OPTIONS]

```
Options:
  --url TEXT                      Enter a valid URL
  --ratio FLOAT                   Ratio to summarize to.
  --algorithm [gensim|spacy|bert]
                                  Algorithm to use
  --help                          Show this message and exit.
```
