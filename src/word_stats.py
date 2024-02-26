"""Helper Module, to rank words by letter commonality"""
def provide_az_list(word_size: int) -> list[dict]:
    az_dict = {}
    az_list = []

    for c in range(ord('a'), ord('z')+1):
        az_dict[chr(c)] = 0

    for i in range(0, word_size):
         az_list.append( az_dict.copy())

    return az_list


def letter_commonality(words: list[str]):
    if not words:
        return {}
    
    az_list_of_occurences = provide_az_list(len(words[0]))

    for word in words:
        for position, letter in enumerate(word):
            az_list_of_occurences[position][letter] += 1
    
    return az_list_of_occurences
    

def rank_words_by_commonality(words: list[str]) -> dict:
    """Entry point, ranks word list and returns dict ordered by commonality.
        N.B. This is dependent upon Python maintaining insert order for dicts.
    """

    analysis = letter_commonality(words)
    word_scoring = {}

    for word in words:
        word_score = 0
        for position, letter in enumerate(word):
            word_score += analysis[position][letter] 
        word_scoring[word] = word_score

    sorted_word_scoring = sorted(word_scoring.items(), key=lambda x:x[1], reverse=True )

    return dict(sorted_word_scoring)
