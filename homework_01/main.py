"""
Домашнее задание №1
Функции и структуры данных
"""
from math import sqrt


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return list(map(lambda x: pow(x, 2), args))


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(num: int):
    # root_number = int(sqrt(num))+1
    if num < 2:
        return False

    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True


def filter_numbers(user_list: list, mask: str):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if mask == EVEN:
        return list(filter(lambda x: x % 2 == 0, user_list))
    elif mask == ODD:
        return list(filter(lambda x: x % 2 == 1, user_list))
    elif mask == PRIME:
        return list(filter(lambda x: is_prime(x), user_list))
