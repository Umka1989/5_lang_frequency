import os.path
import sys
import collections


def load_data(filepath):
    text = []
    if os.path.exists(filepath):
        file = open(filepath, 'r').read()
        for line in file.split('\n'):
            for word in line.split(' '):
                text.append(word)
    return text


def get_most_frequent_words(text):
    frequencies = collections.Counter()
    for word in text:
        if len(word) - 1 == sum(1 for each in word[:-1] if each.isalpha()):
            word = word if word[-1].isalpha() else word[:-1]
            frequencies[word] += 1
    return frequencies


def pprint_for_frequencies_dict(frequencies):
    for key, value in sorted(frequencies.items(), reverse=True, key=lambda x: x[1])[:10]:
        print(key + ' : ' + str(value))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Module need a correct file path as argument')
    else:
        loaded_text = load_data(sys.argv[1])
        frequencies_dict = get_most_frequent_words(loaded_text)
        pprint_for_frequencies_dict(frequencies_dict)
