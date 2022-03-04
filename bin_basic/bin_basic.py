import typing as tp


def find_value(nums: tp.Union[list[int], range], value: int) -> bool:
    """
    Find value in sorted sequence
    :param nums: sequence of integers. Could be empty
    :param value: integer to find
    :return: True if value exists, False otherwise
    """
    left, right = 0, len(nums) - 1
    if right == -1:
        return False
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == value:
            return True
        elif nums[mid] > value:
            right = mid - 1
        else:
            left = mid + 1
    return True if nums[left] == value else False
