from . import hash_table

def index(stems, corpus):
    # Index the given corpus.
    dictionary = hash_table.HashTable()
    for stem in stems:
        dictionary[stem] = [ process_data.path for process_data in corpus if stem in document.stems ]
    # Return the dictionary.
    return dictionary
