# word_guessed = 'never'
# # actual word will be unknown
# actual_word  = 'glove' 

# # this will be passed in as a param
# guess_status = [0,2,2,1,0]

# need an enum most likely.

def add_to_invalid_letters(word, guess_status):

    invalid_letters = []
    for i, val in enumerate(guess_status):
        if val == 0:
            invalid_letters.append(word[i])

    return invalid_letters


def add_to_valid_letters(word, guess_status):

    valid_letters = []
    for i, val in enumerate(guess_status):
        if val == 2 or val == 1:
            valid_letters.append(word[i])

    return valid_letters


def add_to_correct_letter_dict(existing_dict, word, guess_status):

    new_dict = existing_dict
    for i, val in enumerate(guess_status):
        if val == 1:
            new_dict.update({i : word[i]})

    return new_dict

def add_to_correct_letter_dict2(word, guess_status):

    new_dict = {}
    for i, val in enumerate(guess_status):
        if val == 1:
            new_dict.update({i : word[i]})

    return new_dict

def add_to_out_of_place_dict(word, guess_status):

    new_dict = {}
    for i, val in enumerate(guess_status):
        if val == 2:
            new_dict.update({i : word[i]})

    return new_dict



# def add_to_filter_rules(filter_rules, additional_rules):
#     """
#     Adds letters to the existing filter rules, maintaining the existing letters.

#     Parameters:
#     filter_rules (dict): The current filter rules.
#     additional_rules (dict): New rules to add to the existing filter rules.

#     Returns:
#     dict: Updated filter rules.
#     """
#     updated_rules = filter_rules.copy()

#     for position, invalid_chars in additional_rules.items():
#         if position in updated_rules:
#             # Update existing position with new invalid characters, avoiding duplicates
#             updated_rules[position] = list(set(updated_rules[position] + invalid_chars))
#         else:
#             # Add new position with its invalid characters
#             updated_rules[position] = invalid_chars

#     return updated_rules




# print (add_to_invalid_letters(word_guessed, guess_status) )
# print (add_to_valid_letters(word_guessed, guess_status) )


# existing_dict = {
#   0: "_",
#   1: "_",
#   2: "_",
#   3: "_",
#   4: "_"
# }
# print (existing_dict)
# print( add_to_correct_letter_dict(existing_dict, word_guessed, guess_status))

