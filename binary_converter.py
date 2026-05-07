"""Naturalne na binarne"""


def decimal_to_binary(number: int) -> str:
    """Konwertuj liczby"""
    if not isinstance(number, int) or isinstance(number, bool):
        raise ValueError("Liczba musi byc naturalna ")

    if number < 0 or number > 100:
        raise ValueError("Liczba jest poza dozwolonym zakresem (0-100)")

    return bin(number)[2:]
