import typing as tp
from collections import Counter


def get_min_to_drop(seq: tp.Sequence[tp.Any]) -> int:
    """
    :param seq: sequence of elements
    :return: number of elements need to drop to leave equal elements
    """
    if len(seq) == 0:
        return 0
    numbers_frequencies = Counter(seq)
    return sum(numbers_frequencies.values()) - numbers_frequencies.most_common(1)[0][1]
