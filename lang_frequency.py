import os.path
import sys
import collections


def load_data(filepath):
    if os.path.exists(filepath):
        with open(filepath) as source_file:
            unsplited_text = source_file.read()
    return unsplited_text


def splitter(text):
    list_of_words = []
    for line in text.split('\n'):
        for word in line.split(' '):
            list_of_words.append(word.upper())
    return list_of_words


def get_most_frequent_words(text):
    frequencies_counter = collections.Counter()
    for word in text:
        if len(word) - 1 == sum(1 for each in word[:-1] if each.isalpha()):
            word = word if word[-1].isalpha() else word[:-1]
            frequencies_counter[word] += 1
    return frequencies_counter


def pprint_for_frequencies_dict(frequencies_counter):
    """функция принимает на вход счётчик частот слов сортирует анонимной функцией,
    которая в каждой паре "слово: частота" выбирает частоту.
    revers заставляет сортировку работать от большего к меньшему.
    выбирается не более 10 самых частовстречающихся слов и вывыдотся в красивом формате"""
    for word, frequency in sorted(frequencies_counter.items(), reverse=True, key=lambda x: x[1])[:10]:
        print(word + ' : ' + str(frequency))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Module need a correct file path as argument')
    else:
        loaded_text = splitter(load_data(sys.argv[1]))
        frequencies_dict = get_most_frequent_words(loaded_text)
        pprint_for_frequencies_dict(frequencies_dict)
