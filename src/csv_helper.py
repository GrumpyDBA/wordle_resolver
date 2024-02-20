import csv


def read_words_from_csv(filename):
    print("this should not blend")
    words = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            # Assuming each word is in its own row as the first element
            words.append(row[0])
    return words
