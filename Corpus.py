import os
from Document import Document
from concurrent.futures import ThreadPoolExecutor

class Corpus:
    # Constructor
    def __init__(self):
        # List of strings
        self.names = self.read_names(file_path)
        # List of Document objects
        self.documents = self.load_corpus()
        # List of stems
        self.stems = self.get_stems()
        # List of terms
        self.terms = self.get_terms()
        # Write matrix of terms to file_path
        self.write_term_matrix("terms.csv")
        # Write matrix of stems to file_path
        self.write_stemm_matrix("stems.csv")

    # Read files from dir_path and add them to corpus as a list of strings
    def read_names(self, dir_path):
        file_names = os.listdir(dir_path)
        complete_file_names = [os.path.join(dir_path, file_name) for file_name in file_names]
        return complete_file_names

    # Transform each file into a Document object and add it to corpus
    # Here Document class removes stop words and stems the words
    def load_corpus(self):
        with ThreadPoolExecutor() as executor:
            documents = executor.map(Document, self.names)
        return list(documents)

    # Get all terms from corpus
    def get_terms(self):
        terms = []
        for document in self.documents:
            terms += document.terms
        return set(terms)

    # Get all stems from corpus
    def get_stems(self):
        stems = []
        for document in self.documents:
            stems += document.stems
        return set(stems)

    def __write_csv(self, file_path, matrix):
        import csv
        with open(file_path, "w", newline='') as file:
            writer = csv.writer(file)
            for row in data:
                writer.writerow(row)

    # Write matrix of terms to file_path
    def write_term_matrix(self, file_path):
        matrix = [self.terms]
        for document in self.documents:
            row = []
            for term in self.terms:
                if term in document.terms:
                    row.append(1)
                else:
                    row.append(0)
            matrix.append(row)

        self.__write_csv(file_path, matrix)

    # Write matrix of stems to file_path
    def write_stemm_matrix(self, file_path):
        matrix = [self.stems]
        for document in self.documents:
            row = []
            for stem in self.stems:
                if stem in document.stems:
                    row.append(1)
                else:
                    row.append(0)
            matrix.append(row)

        self.__write_csv(file_path, matrix)

    def __str__(self):
        return str(self.documents)

    def __repr__(self):
        return str(self.documents)

    def __len__(self):
        return len(self.documents)

    def __getitem__(self, key):
        return self.documents[key]

    def query(self, query):
        pass


