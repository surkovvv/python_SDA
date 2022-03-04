def merge_iterative(lst_a: list[int], lst_b: list[int]) -> list[int]:
    """
    Merge two sorted lists in one sorted list
    :param lst_a: first sorted list
    :param lst_b: second sorted list
    :return: merged sorted list
    """
    first, second = 0, 0
    n, m = len(lst_a), len(lst_b)
    result = [0] * (n + m)
    while first + second < n + m:
        if first == n:
            a_val = float("inf")
        else:
            a_val = lst_a[first]
        if second == m:
            b_val = float("inf")
        else:
            b_val = lst_b[second]
        if a_val < b_val:
            result[first + second] = a_val
            first += 1
        else:
            result[first + second] = b_val
            second += 1
    return result


def merge_sorted(lst_a: list[int], lst_b: list[int]) -> list[int]:
    """
    Merge two sorted lists in one sorted list ising `sorted`
    :param lst_a: first sorted list
    :param lst_b: second sorted list
    :return: merged sorted list
    """
    return sorted(lst_a + lst_b)


"""
if __name__ == "__main__":
    print(merge_iterative([1, 1, 2, 3], [1, 3, 5]))
    print(merge_iterative([], [1]))
    print(merge_iterative([2], []))
    print(merge_iterative([1], [2]))
    print(merge_iterative([1, 3, 5, 7], [2, 4, 6, 8]))
    print(merge_iterative([], []))
    print(merge_sorted([1, 1, 2, 3], [1, 3, 5]))
    print(merge_sorted([], [1]))
    print(merge_sorted([2], []))
    print(merge_sorted([1], [2]))
    print(merge_sorted([1, 3, 5, 7], [2, 4, 6, 8]))
    print(merge_sorted([], []))
"""
