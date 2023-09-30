from . import postfix_notation

def query(dictionary_stems, raw_query, path_files)
    postfix = postfix_notation.postfix(raw_query)
    return evaluate_query(postfix, dictionary_stems, path_files)

def evaluate_query(stemmed_query, data_dictionary, list_of_files):
    assert isinstance(stemmed_query, list)
    assert isinstance(list_of_files, set)
    operators = ["!", "u", "n"]
    stack = []
    for term in stemmed_query:
        if term not in operators:
            assert isinstance(data_dictionary[term], set)
            stack.append(data_dictionary[term])
        else:
            if term == "!":
                stack.append(complement(stack.pop(), list_of_files))
            elif term == "u":
                stack.append(union(stack.pop(), stack.pop()))
            elif term == "n":
                stack.append(intersect(stack.pop(), stack.pop()))
    return list(stack.pop())

def union(A, B):
    return A.union(B)

def intersect(A, B):
    return A.intersection(B)

def complement(A, universe):
    return set(universe).difference(A)
