"""간단한 문자열 유틸리티."""


def reverse(s: str) -> str:
    """문자열을 뒤집는다."""
    return s[::-1]


def reverse_words(s: str) -> str:
    """단어 순서를 뒤집는다."""
    return " ".join(s.split()[::-1])


def shout(s: str) -> str:
    """대문자 + 느낌표."""
    return s.upper() + "!"
