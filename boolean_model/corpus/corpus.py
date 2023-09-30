import index
import data_preprocessing
import os
from itertools import chain

def read_corpus(path):
    # Read the corpus from the given path.
    files, corpus, stems = read_data(path)
    assert isinstance(corpus, list), "The corpus must be a list of process_data instances."
    assert isinstance(files, list), "The files must be a list of strings path to files."
    dictionary = index.index(stems, corpus)
    # Return the corpus.
    return dictionary, files

def read_data(path):
    # Read the data from the given path.
    files = read_file_paths(path)
    corpus = [ data_preprocessing.process_text.ProcessData(file) for file in files ]
    stems = set( chain.from_iterable( [ process_data.get_stems() for process_data in corpus ] ) )
    # Return the corpus.
    return files, corpus, stems

def read_file_paths(path):
    # Read the file paths from the given path.
    return [ os.path.join(path, file) for file in os.listdir(path) ]

