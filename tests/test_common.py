import string

from beancount_hypothesis import common


def test_currency():
    result = common.currency().example()
    assert len(result) == 3
    assert all([c in string.ascii_uppercase for c in result])

    result = common.currency(["USD", "CAD"]).example()
    assert result in ["USD", "CAD"]


def test_filename():
    result = common.filename().example()
    assert len(result.split("/")) > 1
    assert len(result.split(".")[1]) == 3


def test_word():
    result = common.word().example()
    assert " " not in result
    assert all([c in string.ascii_letters for c in result])


def test_words():
    result = common.words(min=3, max=3).example()
    assert len(result.split(" ")) == 3
