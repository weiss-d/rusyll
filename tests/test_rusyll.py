import pytest

from rusyll import rusyll


test_tokens = [
    "а",
    "б",
    "аа",
    "бб",
    "аб",
    "ба",
    "ар",
    "ра",
    "оно",
    "боб",
    "баржа",
    "званный",
    "карман",
    "карта",
    "карат",
    "Мьянма",
    "майка",
    "майна",
    "фельдъегерь",
    "фильтрпресс",
    "сиреневенький",
    "Йоханнесбург",
    "длинношеее",
    "аорта",
    "Саади",
    "",
]

test_token_reference = [
    ["а"],
    ["б"],
    ["а", "а"],
    ["бб"],
    ["аб"],
    ["ба"],
    ["ар"],
    ["ра"],
    ["о", "но"],
    ["боб"],
    ["ба", "ржа"],
    ["зва", "нный"],
    ["кар", "ман"],
    ["кар", "та"],
    ["ка", "рат"],
    ["Мьян", "ма"],
    ["май", "ка"],
    ["май", "на"],
    ["фель", "дъе", "герь"],
    ["филь", "трпресс"],
    ["си", "ре", "не", "вень", "кий"],
    ["Йо", "ха", "нне", "сбург"],
    ["дли", "нно", "ше", "е", "е"],
    ["а", "ор", "та"],
    ["Са", "а", "ди"],
    [""],
]

test_words = [
    "",
    "а",
    "аа",
    "ааа",
    "-аа",
    "аа-",
    "-а-а-",
    "-",
    "--",
    "--а--а--",
]

test_word_reference = [
    [""],
    ["а"],
    ["а", "а"],
    ["а", "а", "а"],
    ["а", "а"],
    ["а", "а"],
    ["а", "а"],
    [""],
    [""],
    ["а", "а"],
]

test_words_reference_wd = [
    [""],
    ["а"],
    ["а", "а"],
    ["а", "а", "а"],
    ["-", "а", "а"],
    ["а", "а", "-"],
    ["-", "а", "-", "а", "-"],
    ["-"],
    ["-", "-"],
    ["-", "-", "а", "-", "-", "а", "-", "-"],
]


@pytest.mark.syllables
def test_token_to_syllables():
    test_token_results = []
    for token in test_tokens:
        test_token_results.append(rusyll.token_to_syllables(token))
    assert test_token_results == test_token_reference


@pytest.mark.syllables
def test_word_to_syllables():
    test_word_results = []
    for word in test_words:
        test_word_results.append(rusyll.word_to_syllables(word))
    assert test_word_results == test_word_reference


@pytest.mark.syllables
def test_word_to_syllables_safe__normal():
    test_reference_results = []
    test_function_results = []
    for token in test_tokens:
        test_reference_results.append(rusyll.word_to_syllables(token))
    for word in test_words:
        test_reference_results.append(rusyll.word_to_syllables(word))
    for token in test_tokens:
        test_function_results.append(rusyll.word_to_syllables_safe(token))
    for word in test_words:
        test_function_results.append(rusyll.word_to_syllables_safe(word))
    assert test_reference_results == test_function_results


@pytest.mark.parametrize("bad_word", ["аб.", "ab", "а б", "аб💩", "АБZ", "а.б", "аzб"])
def test_word_to_syllables_safe__error(bad_word):
    with pytest.raises(AssertionError):
        rusyll.word_to_syllables_safe(bad_word)


@pytest.mark.syllables
def test_word_to_syllables_safe_wd__normal():
    test_reference_results = []
    test_function_results = []
    for token in test_tokens:
        test_reference_results.append(rusyll.word_to_syllables_wd(token))
    for word in test_words:
        test_reference_results.append(rusyll.word_to_syllables_wd(word))
    for token in test_tokens:
        test_function_results.append(rusyll.word_to_syllables_safe_wd(token))
    for word in test_words:
        test_function_results.append(rusyll.word_to_syllables_safe_wd(word))
    assert test_reference_results == test_function_results


@pytest.mark.parametrize("bad_word", ["аб.", "ab", "а б", "аб💩", "АБZ", "а.б", "аzб"])
def test_word_to_syllables_safe_dw__error(bad_word):
    with pytest.raises(AssertionError):
        rusyll.word_to_syllables_safe_wd(bad_word)
