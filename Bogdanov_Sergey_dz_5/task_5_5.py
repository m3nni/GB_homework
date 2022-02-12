"""
Задание 5
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]
Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.

ВНИМАНИЕ! Используйте стартовый код для своей реализации:

def get_uniq_numbers(src: list):
    pass


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(*get_uniq_numbers(src))
"""


def get_uniq_numbers(src: list):
    r_set = set()
    time_set = set()
    for num in src:
        if not num in time_set:
            r_set.add(num)
        else:
            r_set.discard(num)
        time_set.add(num)

    # решение через цикл for in
    # r_set_sort = []
    # for i in src:
    #     if i in r_set:
    #         r_set_sort.append(i)

    # решение через генераторное выражение
    r_set_sort = [num for num in src if num in r_set]

    return r_set_sort


src = [2, 2, 2, 7, 23, 1, 44, 9, 44, 3, 2, 10, 7, 4, 11, 5, 5]
print(*get_uniq_numbers(src))
