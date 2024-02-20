import pytest
from src import word_guesser as wg

# def test_wordle():
#     # setup
#     list_of_words = ('ab','yes')
#     under_test = wg.filter_strings_by_chars(('a','b'), list_of_words)
#     # under_test.count
#     print(under_test.count)
#     assert under_test.count == 2

def test_word_match_if_empty_dict():
    aword = "aword"
    dict = {}
    under_test = wg.match_letters_in_place2(dict, aword)
    assert(under_test == True)


def test_filters_true_if_match():
    aword = "aword"
    dict = {4: "d", 0:"a"}
    under_test = wg.match_letters_in_place2(dict, aword)
    assert(under_test == True)


def test_filters_false_if_mismatch():
    aword = "aword"
    dict = {1: "x", 4:"d"}
    under_test = wg.match_letters_in_place2(dict, aword)
    assert(under_test == False)


def test_filter_words_if_excluded():
    words = ["aword", "saaas"]
    exclude_chars = ["s", "x"]

    under_test = wg.filter_strings_by_exclude(exclude_chars, words)

    assert(len(under_test) == 1)
    assert(under_test[0] == "aword")


def test_filter_words_if_included():
    words = ["aword", "saaas", "includeonlyme"]
    exclude_chars = ["i", "e"]

    under_test = wg.filter_strings_by_include(exclude_chars, words)

    assert(len(under_test) == 1)
    assert(under_test[0] == "includeonlyme")


def test_filter_words_by_dict():
    words = ["aword", "saaas", "a_exclude_me"] 
    match_dict = {0:"a", 2: "o"}

    under_test = wg.filter_strings_by_match_dict(match_dict, words)

    assert(len(under_test) ==1)
    assert(under_test[0] == "aword")


# def test_filter_rules():

#     word_list = ["apple", "orange", "banana", "grape", "melon"]
#     filter_rules = {1: ['e', 'r'], 0:['a']}  # Disallow 'e' and 'r' at position 1

#     filtered_words = wg.filter_words(word_list, filter_rules)
    

def test_filter_by_oop():

    non_excluded_word = "valid"
    excluded_word = "aword"
    filter_rules = {1: ['e', 'r'], 0:['a']}

    should_not_be_excluded = wg.filter_strings_by_out_of_position(filter_rules, non_excluded_word)
    should_be_excluded = wg.filter_strings_by_out_of_position(filter_rules, excluded_word)

    assert(should_not_be_excluded == True)
    assert(should_be_excluded == False)

