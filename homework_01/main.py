"""
Домашнее задание №1
Функции и структуры данных
"""
from math import sqrt
from faker import Faker

fake = Faker()


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    # list(i**2 for i in args)
    return list(map(lambda x: pow(x, 2), args))


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(num: int):
    # root_number = int(sqrt(num))+1
    if num < 2:
        return False

    for i in range(2, int(sqrt(num))+1):
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
        user_func = lambda x: x % 2 == 0

    elif mask == ODD:
        user_func = lambda x: x % 2 == 1

    elif mask == PRIME:
        user_func = lambda x: is_prime(x)

    return list(filter(user_func, user_list))


if __name__ == '__main__':
    k = fake.pylist(nb_elements=fake.pyint(30, 100), value_types=["int"])

    print(filter_numbers([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 25, 1369], PRIME))
