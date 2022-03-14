import typing as tp


def revert(dct: tp.Mapping[str, str]) -> dict[str, list[str]]:
    """
    :param dct: dictionary to revert in format {key: value}
    :return: reverted dictionary {value: [key1, key2, key3]}
    """
    new_dict : dict[str, list[str]] = {}
    for key, value in dct.items():
        if value not in new_dict:
            new_dict[value] = []
        new_dict[value].append(key)
    return new_dict
