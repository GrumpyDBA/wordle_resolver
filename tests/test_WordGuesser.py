import pytest
from src import WordGuesser as wg

def test_initial_words():
    """Test initializing with initial words."""
    word_list = ["apple", "banana"]
    word_storage = wg.WordGuesser(word_list)

    assert word_storage.get_words() == word_list


def test_add_invalid_letters():
    word_list = ["apple", "banana"]
    word_storage = wg.WordGuesser(word_list)
    word_storage.add_to_invalid_letters("apple", [2,0,0,2,2])

    assert word_storage.invalid_letters == set("p")


def test_add_to_correct_letters():
    word_list = ["apple", "banana"]
    word_storage = wg.WordGuesser(word_list)
    word_storage.add_to_correct_letter_dict("apple", [1,0,1,0,0])

    assert word_storage.correct_letters == {2: 'p', 0: 'a'}
    assert word_storage.words[0] == "apple"


def test_add_to_out_of_place():
    word_list = ["apple", "banana", "apply"]
    word_storage = wg.WordGuesser(word_list)
    word_storage.add_to_out_of_place_dict("apple", [2,0,0,0,0])   

    assert word_storage.out_of_place_letters == {0: 'a'}
    # assert len(word_storage.words) == 1
    # assert word_storage.words[0] == "banana"


def test_full_filtering():
    word_list = ["apple", "banana", "apply", "optac"]
    word_storage = wg.WordGuesser(word_list)
    word_storage.update_word_list_from_guess("apple", [2,1,2,0,0])   
    # TODO; Wordle will show char number 3 as black not yellow. This is a bug I guess in worlde. 
    # Need to handle this gracefully

    assert len(word_storage.words) == 1
    assert word_storage.words[0] == "optac"

def test_filter_word_by_excludes():
    word_list = ["apple", "banana", "apply", "grape"]
    guesser = wg.WordGuesser(word_list)
    guesser.invalid_letters = {'p'}

    assert guesser.filter_word_by_excludes("apple") == False
    assert guesser.filter_word_by_excludes("banana") == True

def test_filter_word_by_includes():
    word_list = ["apple", "banana", "apply", "grape"]
    guesser = wg.WordGuesser(word_list)
    guesser.valid_letters = {'a', 'p'}

    assert guesser.filter_word_by_includes("apple") == True
    assert guesser.filter_word_by_includes("banana") == False

def test_filter_word_by_correct_dict():
    word_list = ["apple", "banana", "apply", "grape"]
    guesser = wg.WordGuesser(word_list)
    guesser.correct_letters = {0: 'a', 2: 'p'}

    assert guesser.filter_word_by_correct_dict("apple") == True
    assert guesser.filter_word_by_correct_dict("banana") == False

def test_filter_words_by_out_of_position():
    word_list = ["apple", "banana", "apply", "grape"]
    guesser = wg.WordGuesser(word_list)
    guesser.out_of_place_letters = {0: 'b', 1: 'n'}

    assert guesser.filter_words_by_out_of_position("banana") == False
    assert guesser.filter_words_by_out_of_position("apple") == True

def test_update_word_list():
    word_list = ["apple", "banana", "apply", "grape", "arppi"]
    guesser = wg.WordGuesser(word_list)
    guesser.update_word_list_from_guess("apple", [1,2,1,0,0])

    assert "apple" not in guesser.get_words()
    assert "banana" not in guesser.get_words()
    assert "arppi" in guesser.get_words()


def test_urger():
    word_list = ["urger", "three", "apply", "grape"]
    guesser = wg.WordGuesser(word_list)
    guesser.update_word_list_from_guess("urger", [0,2,0,1,0])

    assert "urger" not in guesser.get_words()
    assert "banana" not in guesser.get_words()
    assert "three" in guesser.get_words()
