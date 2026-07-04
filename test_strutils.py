from strutils import reverse, reverse_words, shout


def test_reverse():
    assert reverse("abc") == "cba"


def test_reverse_words():
    assert reverse_words("a b c") == "c b a"
    assert reverse_words("hello world") == "world hello"
    assert reverse_words("one") == "one"
    assert reverse_words("") == ""


def test_shout():
    assert shout("hi") == "HI!"
