import os.path
import sys

def load_data(filepath):
    if os.path.exists(filepath):
        text = open(filepath, 'r').read()
        return text


def get_most_frequent_words(text):
    frequencies_dict = {}
    for line in text.split('\n'):
        for word in line.split(' '):
            if len(word) - 1 == sum(1 for any in word[:-1] if any.isalpha()):
                word = word if word[-1].isalpha() else word[:-1]
                if word in frequencies_dict:
                    frequencies_dict[word] += 1
                else:
                    frequencies_dict[word] = 1
    return frequencies_dict

def pprint_for_frequencies_dict(frequencies):
    for key, value in sorted(frequencies.items(), reverse = True, key = lambda x:x[1])[:10]:
        print (key + ' : ' + str(value))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print ('Module need a correct file path as argument')
    else:
        loaded_text = load_data(sys.argv[1])
        frequencies_dict = get_most_frequent_words(loaded_text)
        pprint_for_frequencies_dict(frequencies_dict)
