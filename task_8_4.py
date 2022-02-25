"""
Задание 4
Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения
функции и выбрасывать исключение ValueError, если что-то не так, например:

$ calc_cube(5)
125
$ calc_cube(-5)
Traceback (most recent call last):
  ...
    raise ValueError(msg)
ValueError: wrong val -5
Исключение должно возбуждаться, если значение анализируемого аргумента не является положительным
целочисленным значением, включая 0.

Примечание: сможете ли вы замаскировать работу декоратора?

ВНИМАНИЕ! Используйте стартовый код для своей реализации:

def val_checker(func):
    ...  ## пишите реализацию декоратора здесь


@val_checker()  # не забудьте про аргумент-функцию
def calc_cube(x):
    "" "Возведение числа в третью степень"" "
    return x ** 3


if __name__ == '__main__':
    print(calc_cube(5))
    print(calc_cube('ss'))
"""

from functools import wraps


def val_checker(func_filter):
    def checker(func):
        @wraps(func)
        def decor(x):
            if func_filter(x):
                return func(x)
            raise ValueError(f'wrong value: {x}')
        return decor
    return checker


@val_checker(lambda x: isinstance(x, int) and x > 0)
def calc_cube(x):
    return x ** 3


if __name__ == '__main__':
    print(calc_cube(5))
    print(calc_cube('ss'))
