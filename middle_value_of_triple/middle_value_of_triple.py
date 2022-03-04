def get_middle_value(a: int, b: int, c: int) -> int:
    """
    Takes three values and returns middle value.
    """
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b
    if a > b:
        b, a = a, b
    return b
