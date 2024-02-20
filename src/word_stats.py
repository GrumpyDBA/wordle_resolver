import src.csv_helper as ch
from collections import Counter

def letter_commonality(words):
    # find the most common 5 letters at each particular position.
    if not words:
        return {}

    word_length = len(words[0])
    position_counters = [Counter() for _ in range(word_length)]

    # Count the occurrences of each letter in each position
    for word in words:
        for position, letter in enumerate(word):
            position_counters[position][letter] += 1

    # Determine the most common letter in each position
    most_common_letters = {}
    for position, counter in enumerate(position_counters):
        most_common = counter.most_common(1)[0]  # Get the most common letter and its count
        most_common_letters[position] = most_common

    return most_common_letters




# listofwords = ["Jengo", "alber", "lower","Upper","under"]

# analysis = letter_commonality(listofwords)
# print (analysis)
# for position, (letter, count) in analysis.items():
#     print(f"Position {position + 1}: '{letter}' appears {count} times")
