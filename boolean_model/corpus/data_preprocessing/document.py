import re #regex
import unicodedata # use unicode
import fitz # open pdf

def read_content(path):
    if path.endswith('.pdf'):
        return read_pdf(path)
    elif path.endswith('.txt'):
        return read_txt(path)
    else:
        raise Exception('File format not supported.')

def read_txt(path):
    with open(path, 'r') as file:
        return file.read()

def read_pdf(path):
    file = fitz.open(path)
    content = []
    for page in file:
        content.append(page.get_text())
    return ''.join(content)

def clean_content(content):
        # remove accents
        ## decompose unicode glyphs
        normalized_string = unicodedata.normalize('NFKD',  content)
        ## if a glyhp is compose, use its base form
        no_composed_string = ''.join([c for c in normalized_string if not unicodedata.combining(c)])
        # remove punctuation marks
        no_punctuation_string = re.sub(r'[^\w]+', ' ', no_composed_string)
        # strip text of document to only get the main content
        return no_punctuation_string.strip().lower()

class Document:
    def __init__(self, path_to_doc):
        # set name of document
        self.path = path_to_doc
        # read content of document
        self.content = clean_content( read_content(self.path) )
