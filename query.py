import nltk
from nltk.stem import SnowballStemmer
nltk.download('snowball_data') # Snowball stemmer data
import re
class Query:
    @staticmethod
    def inverse_polish(query):
        operators = ["!", "u", "n", "(", ")"]
        pattern = r'([()!un])|(\b\w+\b)'
        matches = re.findall(pattern, query)
        query = [match[0] or match[1] for match in matches]
        polish = []
        queue = []
        for i in query:
            # si es ) sacar de queue y meter en polish hasta encontrar (
            # print(f"{queue=}")
            # print(f"{polish=}")
            if i == ")":
                op = queue.pop()
                while op != "(":
                    polish.append(op)
                    op = queue.pop()
            # si es operador meter en queue
            elif i in operators:
                queue.append(i)
            # si es otro meter en polish
            else:
                polish.append(i)

        # append the last operand when finishing if expression not englobed by parenthesis
        if queue:
            polish.append(queue.pop())

        return polish

    @staticmethod
    def stem_polish_query(polish):
        stemmer = SnowballStemmer("spanish")
        for i, term in enumerate(polish):
            if term not in ["!", "u", "n"]:
                polish[i] = stemmer.stem(term)
        return polish

    @staticmethod
    def stemmed_query(raw_query):
        ipq = inverse_polish(raw_query)
        return stem_polish_query(ipq)

    @staticmethod
    def union(A, B):
        return A.union(B)

    @staticmethod
    def intersect(A, B):
        return A.intersection(B)

    @staticmethod
    def complement(A, universe):
        return set(universe).difference(A)

    @staticmethod
    def get_query(stemmed_query, data_dictionary, list_of_files):
        list_of_files = set( list_of_files  )
        operators = ["!", "u", "n"]
        stack = []
        for term in stemmed_query:
            if term not in operators:
                stack.append(set(data_dictionary.find( term )))
            else:
                if term == "!":
                    stack.append(complement(stack.pop(), list_of_files))
                elif term == "u":
                    stack.append(union(stack.pop(), stack.pop()))
                elif term == "n":
                    stack.append(intersect(stack.pop(), stack.pop()))
        return list(stack.pop())

    @staticmethod
    def __get_query_from_raw(raw_query, data_dictionary, list_of_files):
        spq = stemmed_query(raw_query)
        return get_query(spq, data_dictionary, list_of_files)

    @staticmethod
    def get(raw_query, data_dictionary, list_of_files):
        return __get_query_from_raw(raw_query, data_dictionary, list_of_files)


if __name__ == "__main__":
    query = input("Introduce query: ") or "!(CACA u (PEOPEO n (CACA u PEOPEO)))"
    ipq = inverse_polish(query)
    print(ipq)
    spq = stem_polish_query(ipq)
    print(spq)
    print(get_query(spq, None, None))
print("restart")
