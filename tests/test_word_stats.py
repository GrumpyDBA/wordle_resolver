import pytest
from unittest import TestCase
from src import word_stats as ws

def test_word_ranking():
    """Test ranking with a few words"""

    listofwords = ["jengo", "lower","upper" , "lowes"]
    actual = ws.rank_words_by_commonality(listofwords)
    expected = {'lower': 11, 'lowes': 10, 'upper': 8, 'jengo': 5}
    TestCase().assertDictEqual(expected, actual)
