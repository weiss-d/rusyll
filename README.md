# rusyll
 Python 3 package for dividing Russian words into phonetic syllables.
## About
This package provides algorithmic phonetic syllable division for Russian language, similar to [nltk SyllableTokenizer](https://github.com/nltk/nltk/blob/develop/nltk/tokenize/sonority_sequencing.py), but adding some language-specific rules.

In fact, there are no unified rules for breaking words into syllables in Russian. Therefore I've selected the most applicable rule set developed by R. I. Avanesov, professor of MSU, in 50s. In short it's based on the sonority index of the letters.

This package can be useful for various Natural Language applications. However, it is not suitable for hyphenation.

## Installation
`pip install rusyll`


## How to use

```python
>>> from rusyll import rusyll
>>> rusyll.token_to_syllables("черепаха")
['че', 'ре', 'па', 'ха']
>>> rusyll.word_to_syllables("черепаха-гофер")
['че', 'ре', 'па', 'ха', 'го', 'фер']
>>> rusyll.word_to_syllables_wd("черепаха-гофер")
['че', 'ре', 'па', 'ха', '-', 'го', 'фер']
>>> rusyll.word_to_syllables_safe("черепаха гофер")
>>> Traceback (most recent call last):
File "<stdin>", line 1, in <module>
File "/home/toor_2/wonder/Python/rusyll/src/rusyll/rusyll.py",
line 125, in word_to_syllables_safe
assert bool(AssertionError: Word contains unsuitable symbols
>>> rusyll.word_to_syllables_safe("черепаха-гофер")
['че', 'ре', 'па', 'ха', 'го', 'фер']
>>> help(rusyll)
#...complete description of functions
```
## Feedback
This is my first attempt to make proper package for PyPI, so any feedback is highly appreciated!
