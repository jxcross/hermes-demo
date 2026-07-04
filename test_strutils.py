from strutils import reverse, shout, slugify


def test_reverse():
    assert reverse("abc") == "cba"


def test_shout():
    assert shout("hi") == "HI!"


def test_slugify():
    assert slugify("Hello World") == "hello-world"
    assert slugify("HELLO WORLD") == "hello-world"
    assert slugify("hello") == "hello"
    assert slugify("") == ""
    assert slugify("  Hello   World  ") == "hello-world"
    assert slugify("Hello\tWorld") == "hello-world"
