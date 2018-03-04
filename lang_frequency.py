import os.path
import sys
import collections


def load_data(filepath):
    if os.path.exists(filepath):
        with open(filepath) as source_file:
            unsplited_text = source_file.read()
        return unsplited_text


def split_text_to_list(unsplited_text):
    list_of_formatted_words = []
    for word in unsplited_text.upper().split():
        count_alphabetical_symbols = sum(1 for symbol
                                         in word if symbol.isalpha())
        if len(word) == count_alphabetical_symbols:
            list_of_formatted_words.append(word)
        elif len(word) - count_alphabetical_symbols == 1:
            word = word[:-1]
            if word:
                list_of_formatted_words.append(word)
    return list_of_formatted_words


def get_most_frequent_words(list_of_words, number_of_most_frequent_word=10):
    frequencies_counter = collections.Counter(list_of_words)
    most_frequent_words = frequencies_counter.most_common(
        number_of_most_frequent_word)
    return most_frequent_words


def print_for_most_frequent_words(most_frequent_words):
    print('{} most frequent words'.format(len(most_frequent_words)))
    for word, _ in most_frequent_words:
        print(word)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Module need a correct file path as argument')
    else:
        file_content = load_data(sys.argv[1])
        list_of_words = split_text_to_list(file_content)
        most_frequent_words = get_most_frequent_words(list_of_words)
        print_for_most_frequent_words(most_frequent_words)
