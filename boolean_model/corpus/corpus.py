from .index import index
from .data_preprocessing import process_text
import os
from itertools import chain

from concurrent.futures import ThreadPoolExecutor

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
    corpus = concurrent_read(files)
    stems = set( chain.from_iterable( [ process_data.get_stems() for process_data in corpus ] ) )
    # Return the corpus.
    return files, corpus, stems

def concurrent_read(files):
    with ThreadPoolExecutor(max_workers=len(files)) as executor:
        corpus = executor.map(lambda file: process_text.ProcessData(file), files)
        return list(corpus)

def read_file_paths(path):
    # Read the file paths from the given path.
    return [ os.path.join(path, file) for file in os.listdir(path) ]

