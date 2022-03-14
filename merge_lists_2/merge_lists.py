import typing as tp
import heapq


def merge(seq: tp.Sequence[tp.Sequence[int]]) -> list[int]:
    """
    :param seq: sequence of sorted sequences
    :return: merged sorted list
    """
    heap : tp.List[tp.Tuple[int, int, int]] = []
    flatten_seq = []
    for i in range(len(seq)):
        if len(seq[i]):
            heapq.heappush(heap, (seq[i][0], i, 0))  # value, iterator's index, <- his index
    while len(heap) > 0:
        to_insert, iterator, index = heapq.heappop(heap)
        if len(seq[iterator]) != index + 1:
            heapq.heappush(heap, (seq[iterator][index + 1], iterator, index + 1))
        flatten_seq.append(to_insert)

    return flatten_seq
