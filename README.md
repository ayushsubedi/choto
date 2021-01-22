### Term Article Summary

#### Installation

`pip install choto`

[![asciicast](https://asciinema.org/a/r203CswsNWHaThJmHLKgpVl60.svg)](https://asciinema.org/a/r203CswsNWHaThJmHLKgpVl60)


### Installation (from source)

#### Clone the repository

`git clone https://github.com/ayushsubedi/choto`

#### CD into the cloned directory and create a virtualenv

`python -m venv env`

### Enable virtualenv

`.\env\Scripts\activate`

### Install dependency packages from requirements.txt

`pip install -r requirements.txt`

### Run the app

`python choto.py --url=https://abc.xyz --ratio=0.5 --algorithm=bert`

Usage: choto.py [OPTIONS]

```
Options:
--url TEXT                      Enter a valid URL
--ratio FLOAT                   Ratio to summarize to.
--algorithm [gensim|spacy|bert] Algorithm to use
--help                          Show this message and exit.
```
