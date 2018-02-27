import os.path
import sys
import collections


def load_data(filepath):
    if os.path.exists(filepath):
        with open(filepath) as source_file:
            unsplited_text = source_file.read()
    return unsplited_text


def text_to_list(unsplited_text):
    #return formatted list of words without digits and punctuation marks
    list_of_words = []
    for line in unsplited_text.upper().split('\n'):
        for word in line.split(' '):
            if len(word) - 1 == sum(1 for each in word[:-1] if each.isalpha()):
                #for words with punctuation marks on the end
                word = word if word[-1].isalpha() else word[:-1]
                list_of_words.append(word)
    return list_of_words


def get_most_frequent_words(list_of_words, number_of_most_frequent_word=10):
    frequencies_counter = collections.Counter(list_of_words)
    ten_most_frequent_word = frequencies_counter.most_common(number_of_most_frequent_word)
    return ten_most_frequent_word


def pprint_for_most_frequent_words(most_frequent_words):
    print("{} most frequent words".format(str(len(most_frequent_words))))
    for word, frequency in most_frequent_words:
        print(word)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Module need a correct file path as argument')
    else:
        file_content = load_data(sys.argv[1])
        list_of_words = text_to_list(file_content)
        most_frequent_word = get_most_frequent_words(list_of_words)
        pprint_for_most_frequent_words(most_frequent_word)

