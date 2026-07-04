"""간단한 문자열 유틸리티."""


def reverse(s: str) -> str:
    """문자열을 뒤집는다."""
    return s[::-1]


def shout(s: str) -> str:
    """대문자 + 느낌표."""
    return s.upper() + "!"


def slugify(s: str) -> str:
    """문자열을 소문자 슬러그로 변환한다."""
    return "-".join(s.lower().split())
