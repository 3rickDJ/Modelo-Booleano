import pytest
import query

def test_inverse_polish_notation():
    list_of_raw_queries =              ["( A u B )",     "(!( A u B ) ) u C",           "( A u B ) u ( C u D )",              "(A u B) u (C u D)"]
    list_of_inverse_polish_notation = [["A", "B", "u"], ["A", "B", "u", "!", "C", "u"], ["A", "B", "u", "C", "D", "u", "u"], ["A", "B", "u", "C", "D", "u", "u"]]

    for raw_query, inverse_polish_notation in zip(list_of_raw_queries, list_of_inverse_polish_notation):
        print(raw_query, inverse_polish_notation)
        assert query.inverse_polish(raw_query) == inverse_polish_notation

def test_stem_polish_query():
    list_of_inverse_polish_notation = [["PERRO", "GATO", "u"], ["CANCION", "BOULEVARD", "u", "!", "CANCION", "u"]]
    list_of_stemmed_queries =         [['perr', 'gat', 'u'], ['cancion', 'boulevard', 'u', '!', 'cancion', 'u']]

    for inverse_polish_notation, stemmed_query in zip(list_of_inverse_polish_notation, list_of_stemmed_queries):
        assert query.stem_polish_query(inverse_polish_notation) == stemmed_query

def test_stemmed_query():
    raw_input = "(( PERRO u COCHE ) u ( AUTO u AUTOMOVIL ))"
    stemmed_query = ['perr', 'coch', 'u', 'aut', 'automovil', 'u', 'u']
    assert query.stemmed_query(raw_input) == stemmed_query

def test_get_query():
    pass

def test_union():
    A = { "A", "B", "C" }
    B = { "A", "B", "D" }
    union = { "A", "B", "C", "D" }
    assert query.union([A, B]) == union

def test_intersect():
    A = { "A", "B", "C" }
    B = { "Z", "B", "D" }
    intersection = { "B" }
    assert query.intersect([A, B]) == intersection

def test_complement():
    universe = ["A", "B", "C", "D"]
    A = { "A", "B", "C" }
    A_complement = { "D" }
    assert query.complement(A, universe) == A_complement

