"""Collection of functions for splitting Russian words into phonetic syllables.

This package provides algorithmic phonetic syllable division for Russian
language, similar to nltk SyllableTokenizer, but adding some
language-specific rules.

In fact, there are no unified rules for breaking words into syllables in Russian. Therefore I've selected the most applicable rule set developed by R. I. Avanesov, professor of MSU, in 50s. In short it's based on the sonority index of the letters.

This package can be useful for various Natural Language applications.
However, it is not suitable for hyphenation.

See function docstrings for details.
"""

import re

from typing import List


def token_to_syllables(token: str) -> List[str]:
    """Split a Russian token into syllables.

    Base function of the module.
    No protection - use word_to_syllables() when words with dashes occure
    at the input and word_to_syllables_safe() to check
    for unsuitable symbols.

    Args:
        token: tokenized word. Only Russian letters allowed uppercase
            or lowercase, no dashes, spaces or other symbols.

    Returns:
        A list of syllables.
    """
    if len(token) < 2:
        return [token]

    VOWELS = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    UNPAIRED_SONANTS = "рлмнРЛМН"
    SIGNS = "ьъЬЪ"

    break_indices = [i + 1 for i, letter in enumerate(token) if letter in VOWELS]
    if len(break_indices) < 2:
        return [token]

    for i, indice in enumerate(break_indices[:-1]):
        letter = token[indice]
        next_letter = token[indice + 1 : indice + 2]
        # Slice is used to defeat IndexError on last letter

        if (
            letter in UNPAIRED_SONANTS
            and next_letter not in VOWELS
            and letter != next_letter
            and not (letter in "рР" and next_letter in "жЖ")
            and next_letter not in SIGNS
        ):
            break_indices[i] += 1
        elif letter in UNPAIRED_SONANTS and next_letter in SIGNS:
            break_indices[i] += 2
        elif letter in "йЙ" and next_letter not in VOWELS:
            break_indices[i] += 1

    break_indices.insert(0, 0)
    del break_indices[-1]

    return [token[i:j] for i, j in zip(break_indices, break_indices[1:] + [None])]


def word_to_syllables(word: str) -> List[str]:
    """Split a Russian word into syllables.

    Main function of the module to be used in most cases including
    compound words with dashes. Dashes are not included in the output,
    e.g., "Как-нибудь" -> ["Как", "ни", "будь"]
    Use word_to_syllables_wd to include dashes in output as a separate
    syllables.

    Arguments:
        word: a word consisting of Russian letters (uppercase or lowercase)
            and dashes. No spaces and other symbols allowed.

    Returns:
        A list of syllables.
    """
    syllables = []

    for subword in word.split("-"):
        if subword:
            syllables += token_to_syllables(subword)

    if not syllables: syllables = [""]
    return syllables


def word_to_syllables_wd(word: str) -> List[str]:
    """Split a Russian word into syllables and include dashes in output.

    Dases are included as separate syllables.
    E.g., "Как-нибудь" -> ["Как", "-", "ни", "будь"]

    Arguments:
        word: a word consisting of Russian letters (uppercase or lowercase)
            and dashes. No spaces and other symbols allowed.

    Returns:
        A list of syllables.
    """
    syllables = []

    for subword in word.split("-"):
        if subword:
            syllables += token_to_syllables(subword) + ["-"]
        else:
            syllables.append("-")

    return syllables[:-1]


def word_to_syllables_safe(word: str) -> List[str]:
    """Split a Russian word into syllables with assertion.

    Asserts that word contains only correct symblos.
    Dashes aren't included in the output.

    Arguments:
        word: a string presumably containing a Russian word.

    Returns:
        A list of syllables.

    Raises:
        AssertionError: Word contains unsuitable symbols:
            spaces, English letters ets.
    """
    assert bool(
        re.match(r"\A[а-яА-ЯёЁьЬъЪ-]*\Z", word)
    ), "Word contains unsuitable symbols"

    return word_to_syllables(word)


def word_to_syllables_safe_wd(word: str) -> List[str]:
    """Split a Russian word into syllables with assertion.

    Asserts that word contains only correct symblos.
    Dashes included in the output.

    Arguments:
        word: a string presumably containing a Russian word.

    Returns:
        A list of syllables.

    Raises:
        AssertionError: Word contains unsuitable symbols:
            spaces, English letters ets.
    """
    assert bool(
        re.match(r"\A[а-яА-ЯёЁьЬъЪ-]*\Z", word)
    ), "Word contains unsuitable symbols"
    assert bool(
        re.match(r"\A[а-яА-ЯёЁьЬъЪ-]*\Z", word)
    ), "Word contains unsuitable symbols"

    return word_to_syllables_wd(word)


def main() -> None:
    """Print out the syllables of a single word taken from user input."""
    word = input("Word: ")
    print(word_to_syllables_safe(word), word_to_syllables_safe_wd(word))


if __name__ == "__main__":
    main()
