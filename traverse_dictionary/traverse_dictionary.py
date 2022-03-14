import typing as tp
from collections import deque


def traverse_dictionary_immutable(
        dct: tp.Mapping[str, tp.Any],
        prefix: str = "") -> list[tuple[str, int]]:
    """
    :param dct: dictionary of undefined depth with integers or other dicts as leaves with same properties
    :param prefix: prefix for key used for passing total path through recursion
    :return: list with pairs: (full key from root to leaf joined by ".", value)
    """
    result: list[tuple[str, int]] = []

    def dfs(root_dct: tp.Any, prefix: str = "") -> None:
        if type(root_dct) is int:
            result.append((prefix, root_dct))
            return
        new_pref = prefix + "." if prefix else prefix
        for key in root_dct:
            dfs(root_dct[key], new_pref + key)
    dfs(dct, prefix)
    return result


def traverse_dictionary_mutable(
        dct: tp.Mapping[str, tp.Any],
        result: list[tuple[str, int]],
        prefix: str = "") -> None:
    """
    :param dct: dictionary of undefined depth with integers or other dicts as leaves with same properties
    :param result: list with pairs: (full key from root to leaf joined by ".", value)
    :param prefix: prefix for key used for passing total path through recursion
    :return: None
    """
    def dfs(root_dct: tp.Any, result: list[tuple[str, int]], prefix: str = "") -> None:
        if type(root_dct) is int:
            result.append((prefix, root_dct))
            return
        new_pref = prefix + "." if prefix else prefix
        for key in root_dct:
            dfs(root_dct[key], result, new_pref + key)
    dfs(dct, result, prefix)


def traverse_dictionary_iterative(
        dct: tp.Mapping[str, tp.Any]
        ) -> list[tuple[str, int]]:
    """
    :param dct: dictionary of undefined depth with integers or other dicts as leaves with same properties
    :return: list with pairs: (full key from root to leaf joined by ".", value)
    """
    stack: tp.Deque[tuple[tp.Any, str]] = deque()
    result: list[tuple[str, int]] = []
    prefix: str = ""
    stack.append((dct, prefix))
    while stack:
        root_dict, prefix = stack.pop()
        if prefix:
            prefix = prefix + "."
        for key in root_dict:
            if type(root_dict[key]) is int:
                result.append((prefix + key, root_dict[key]))
            else:
                stack.append((root_dict[key], prefix + key))
    return result
