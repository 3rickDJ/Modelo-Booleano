from corpus import corpus
from query import query

class BooleanModel:
    def __init__(self, path="documentos/"):
        self.boolean_model(path)


    # Loads the corpus
    def boolean_model(self, path="documentos/"):
        # Read the corpus
        # Store in dictionary_stems the retrieved dictionary of stems -> documents
        # Store in path_files the retrieved list of paths to the documents
        self.dictionary_stems, self.path_files = corpus.read_corpus(path)

    def query(self, raw_query):
        # Return the list of documents that satisfy the query
        return query.query(self.dictionary_stems, raw_query, self.path_files)
