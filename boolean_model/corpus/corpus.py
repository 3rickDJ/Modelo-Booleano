from .index import index
from .data_preprocessing import process_text
import os
from itertools import chain

from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor

def read_corpus(path):
    # Read the corpus from the given path.
    files, corpus, stems = read_data(path)
    assert isinstance(corpus, list), "The corpus must be a list of process_data instances."
    assert isinstance(files, list), "The files must be a list of strings path to files."
    assert isinstance(corpus[0], process_text.ProcessData), "The corpus must be a list of process_data instances."
    dictionary = index.index(stems, corpus)
    # Return the corpus.
    return dictionary, files

def read_data(path):
    # Read the data from the given path.
    files = read_file_paths(path)
    corpus = concurrent_read(files)
    stems = set( chain.from_iterable(concurrent_stems(corpus)) )
    update_corpus_stems(corpus, stems)
    # Return the corpus.
    return files, corpus, stems

def concurrent_read(files):
    with ThreadPoolExecutor(max_workers=len(files)) as executor:
        corpus = executor.map(lambda file: process_text.ProcessData(file), files)
        return list(corpus)

def concurrent_stems(corpus):
    with ProcessPoolExecutor() as executor:
        stems = executor.map(get_stem_instance, corpus)
        return list(stems)

def get_stem_instance(process_data):
    return process_data.get_stems()

def update_corpus_stems(corpus, stems):
    for process_data in corpus:
        process_data.stems = stems

def read_file_paths(path):
    # Read the file paths from the given path.
    return [ os.path.join(path, file) for file in os.listdir(path) ]

