# Frequency Analysis of Words

This is tool for frequency analysis of words

# How to use
Like imported module in python:
```python
from lang_frequency import get_most_frequent_words, text_to_list
list_of_words = text_to_list(some_text)
result = get_most_frequent_words(list_of_words)
```

Like independent application with bash
```bash
python lang_frequency.py file_with_text.txt
```
You need Python 3+ interpreter

# Result of using and example

Result of using program is a dictionary with 10 or less (for text shorter then 10 words) words with if frequency

Example:

```python
Counter({'CAT': 3, 'DOG': 2, 'RAT': 1})
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
