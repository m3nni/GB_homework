"""
Задание 4
Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [12, 44, 4, 10, 78, 123]
Подсказка: использовать возможности python, изученные на уроке. Подумайте, как можно сделать
оптимизацию кода по памяти, по скорости.

ВНИМАНИЕ! Используйте стартовый код для своей реализации:

def get_numbers(src: list):
    pass


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(*get_numbers(src))
"""

def get_numbers(src: list):

    # вариант № 1
    #i = 1
    #result = []
    #while i != len(src):
    #    second_el = src[i]
    #    first_el = src[i - 1]
    #    if second_el > first_el:
    #        result.append(second_el)
    #    i += 1

    # вариант № 2

    new_src = src[1:]
    result = [new_src[i] for i in range(len(new_src)) if new_src[i] > src[i]]

    return result


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(*get_numbers(src))
