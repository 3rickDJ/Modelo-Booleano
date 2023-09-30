from .hash_table import HashTable
def index(stems, corpus):
    # Index the given corpus.
    dictionary = HashTable()
    for stem in stems:
        dictionary[stem] = set( [ process_data.path for process_data in corpus if stem in process_data.stems ] )
    # Return the dictionary.
    return dictionary
