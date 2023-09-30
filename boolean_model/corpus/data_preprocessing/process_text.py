from . import document

import nltk # natural language toolkit
from nltk.corpus import stopwords # stopwords import fitz # open pdf
nltk.download('stopwords', quiet=True) # stopwords data
from nltk.stem import SnowballStemmer
nltk.download('snowball_data', quiet=True) # Snowball stemmer data

import re # regular expressions

def tokenize(document):
    return re.split(r'[^\w]+', document)

def remove_stop_words(terms):
    # Clean the given document.
    clean_terms =  [ w for w in terms if not is_stop_word(w) ]
    return clean_terms

def is_stop_word(word):
    return word in stopwords.words('spanish') or len(word) <= 3

def stem(cleaned_terms):
    # Stem the given document.
    stemmer = SnowballStemmer("spanish")
    stems = [stemmer.stem(t) for t in cleaned_terms]
    return set(stems)

class ProcessData():
    def __init__(self, path):
        self.path = path
        self.document = document.Document(path)
        self.stems = self.get_stems()

    def get_stems(self):
        tokens = tokenize(self.document.content)
        clean_tokens = clean(tokens)
        self.terms = set(clean_tokens)
        stems = stem(clean_tokens)
        return stems
