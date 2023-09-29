import nltk # natural language toolkit
from nltk.corpus import stopwords # stopwords import fitz # open pdf
import re #regex
import unicodedata # use unicode
nltk.download('stopwords', quiet=True) # stopwords data
nltk.download('punkt', quiet=True) # tokenizer data
nltk.download('snowball_data', quiet=True) # Snowball stemmer data
from nltk.stem import SnowballStemmer

class Document:
    def __init__(self, path_to_doc):
        # set name of document
        self.doc_name = path_to_doc
        # read content of document
        self._content()
        # get unique terms in document
        self.terms = self.terms_unique(self.content)
        # get stems in document
        self.stems = self.stemming()

    def _content(self):
        raw_doc = self._read_raw_doc(self.doc_name)
        content = self._clean_doc(raw_doc)
        self.content = content

    def _freq(self):
        self.freq_table = self.freq_term_table(self.terms(self.content))
        self.terms = self.terms_unique(self.content)


    def __str__(self):
        return f"{self.doc_name}"

    def remove_stop_words(self):
        self.clean_terms =  [ w for w in self.terms if not self.is_stop_word(w) ]
        return self.clean_terms

    def is_stop_word(self, word):
        return word in stopwords.words('spanish') or len(word) <= 3

    def stemming(self):
        self.remove_stop_words()
        stemmer = SnowballStemmer("spanish")
        self.stems = [stemmer.stem(t) for t in self.clean_terms]
        return self.stems

    def terms(self, clean_document):
        return re.split(r'[^\w]+', clean_document)

    def terms_unique(self, clean_document):
        splited_words = self.terms(clean_document)
        terms = []
        for w in splited_words:
            if w not in terms:
                terms.append(w)
        return terms

    def freq_term_table(self, terms):
        freq_table = {}
        for term in terms:
            if term in freq_table:
                freq_table[term] += 1
            else:
                freq_table[term] = 1
        return freq_table

    def _read_raw_doc(self, doc_name):
        doc = fitz.open(doc_name)
        text = []
        for page in doc:
            text.append(page.get_text())
        return ''.join(text)

    def _clean_doc(self, raw_doc):
        # remove accents
        ## decompose unicode glyphs
        normalized_string = unicodedata.normalize('NFKD',  raw_doc)
        ## if a glyhp is compose, use its base form
        no_accent_string = ''.join([c for c in normalized_string if not unicodedata.combining(c)])
        # remove punctuation marks
        no_punctuation_string = re.sub(r'[^\w]+', ' ', no_accent_string)
        # strip text of document to only get the main content
        return no_punctuation_string.strip().lower()
