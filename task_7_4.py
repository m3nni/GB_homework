"""Задание 4
Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи —
верхняя граница размера файла (пусть будет кратна 10), а значения — общее количество файлов
(в том числе и в подпапках), размер которых не превышает этой границы, но больше предыдущей (начинаем с 0),
например:

{
  100: 15,
  1000: 3,
  10000: 7,
  100000: 2
}
Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...

Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
"""

import os
import sys
from pprint import pprint

size = {}

def size_files(path):

    for root, dirs, files in os.walk(path):
        for file in files:
            r_file = os.path.join(root, file)
            st_sizes = 10 ** len(str(os.stat(r_file).st_size))
            size[st_sizes] = size.get(st_sizes, 0) + 1


if __name__ == "__main__":

    if len(sys.argv) == 2:
        path = sys.argv[1]
    else:
        path = os.getcwd()
    size_files(path)
    pprint(size, width=1)
