# Frequency Analysis of Words

This is tool for frequency analysis of words

# How to use
Like imported module in python:
```python
from lang_frequency import get_most_frequent_words, split_text_to_list

list_of_words = split_text_to_list(some_text)
result = get_most_frequent_words(list_of_words, number_of_most_common_words)
```

Like independent application with bash
```bash
python lang_frequency.py file_with_text.txt
```
You need Python 3+ interpreter

# Result of using

Result of using program is a list of tuple with words and it's frequency (with using model's funtions) or just most common words (if you use it like independed progrmm)  

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
