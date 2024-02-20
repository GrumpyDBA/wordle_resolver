# Note that although we maintain the state of valid invalid characters,
# we don't technically need to, as the list of words is completely filtered each time it runs.
# If I did this again, I would probably do it like this:
# 1. update the lists etc of valid/invalid.
# 2. iterate the word list 
# 3. pass each word through functions for valid/invalid, then remove based upon this. less iterations and faster.


# TODO; In test case below:
# Wordle will show char number 3 as black not yellow. This is a "bug" of sorts I guess in worlde. 
# Need to handle this gracefully: this is the test case to use
# word_list = ["apple", "banana", "apply", "optac"]
# word_storage = wg.WordGuesser(word_list)
# word_storage.update_word_list("apple", [2,1,2,0,0]) 
# versus 
# word_storage.update_word_list("apple", [2,1,0,0,0]) 
# Likely want to handle via input validation 

from typing import List, Set, Dict

class WordGuesser:

    def __init__(self, word_list: List[str]):
        self.words: List[str] = word_list
        self.invalid_letters: Set[str] = set()
        self.valid_letters: Set[str] = set()
        self.correct_letters: Dict[int, str] = {}
        self.out_of_place_letters: Dict[int, str] = {}

    def get_words(self) -> List[str]:
        return self.words

    def update_word_list_from_guess(self, word_guess: str, guess_status: List[int]) -> None:
        self.add_to_valid_letters(word_guess, guess_status)
        self.add_to_invalid_letters(word_guess, guess_status)
        self.add_to_correct_letter_dict(word_guess, guess_status)
        self.add_to_out_of_place_dict(word_guess, guess_status)

        self.words = self.filter_word_list_by_all_factors()

    def filter_word_list_by_all_factors(self) -> List[str]:
        filtered_words: List[str] = []
        for word in self.words:
            if (
                self.filter_word_by_excludes(word) and
                self.filter_word_by_includes(word) and
                self.filter_word_by_correct_dict(word) and 
                self.filter_words_by_out_of_position(word)
                ):
                filtered_words.append(word)

        return filtered_words

    def filter_word_by_excludes(self, word: str) -> bool:
        return not any(char in word for char in self.invalid_letters)
    
    def filter_word_by_includes(self, word: str) -> bool:
        return all(char in word for char in self.valid_letters)

    def filter_word_by_correct_dict(self, word: str) -> bool:
        return all(self.correct_letters[key] == word[key] for key in self.correct_letters)
    
    def filter_words_by_out_of_position(self, word: str) -> bool:
        return all(word[position] not in invalid_chars 
                   for position, invalid_chars in self.out_of_place_letters.items()
                   if position < len(word))

    def add_to_invalid_letters(self, word_guess: str, guess_status: List[int]) -> None:
        for i, val in enumerate(guess_status):
            if val == 0 and word_guess[i] not in self.valid_letters:
                self.invalid_letters.add(word_guess[i])

    def add_to_valid_letters(self, word_guess: str, guess_status: List[int]) -> None:
        for i, val in enumerate(guess_status):
            if val in [1, 2]:
                self.valid_letters.add(word_guess[i])

    def add_to_correct_letter_dict(self, word_guess: str, guess_status: List[int]) -> None:
        new_dict: Dict[int, str] = {}
        for i, val in enumerate(guess_status):
            if val == 1:
                new_dict[i] = word_guess[i]

        self.correct_letters.update(new_dict)

    def add_to_out_of_place_dict(self, word_guess: str, guess_status: List[int]) -> None:
        new_dict: Dict[int, str] = {}
        for i, val in enumerate(guess_status):
            if val == 2:
                new_dict[i] = word_guess[i]

        self.out_of_place_letters.update(new_dict)
