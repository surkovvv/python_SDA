import typing as tp


def filter_list_by_list(lst_a: tp.Union[list[int], range], lst_b: tp.Union[list[int], range]) -> list[int]:
    """
    Filter first sorted list by other sorted list
    :param lst_a: first sorted list
    :param lst_b: second sorted list
    :return: filtered sorted list
    """
    first, second = 0, 0
    result = []
    size = len(lst_a) + len(lst_b)
    while first + second < size:
        if first == len(lst_a):
            break
        if second == len(lst_b):
            while first < len(lst_a):
                result.append(lst_a[first])
                first += 1
            break
        if lst_a[first] == lst_b[second]:
            first += 1
        elif lst_a[first] > lst_b[second]:
            second += 1
        else:
            result.append(lst_a[first])
            first += 1
    return result


"""
if __name__ == "__main__":
    print(filter_list_by_list([1, 1, 2, 3, 7], [1, 3, 5]))
    print(filter_list_by_list([1, 1, 1, 2], [1]))
    print(filter_list_by_list([1, 1, 1], [1]))
    print(filter_list_by_list([1, 2, 3], []))
    print(filter_list_by_list([], [1, 2, 3, 4]))
"""
