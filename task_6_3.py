"""
Задание 3
Есть два файла users.csv и hobby.csv: в первом хранятся ФИО пользователей сайта,
а во втором — данные об их хобби. Известно, что при хранении данных используется принцип:
одна строка — один пользователь, разделитель между значениями — запятая.
Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО,
значения — данные о хобби (список строковых переменных). Сохранить словарь в файл task_6_3_result.json.
Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО,
задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом 1.

При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.

Фрагмент файла с данными о пользователях (users.csv):

Иванов,Иван,Иванович
Петров,Петр,Петрович
Фрагмент файла с данными о хобби (hobby.csv):

скалолазание,охота
горные лыжи
ВНИМАНИЕ! Используйте стартовый код для своей реализации:

import sys
import json


def prepare_dataset(path_users_file: str, path_hobby_file: str) -> dict:
    тут три кавычки
    Считывает данные из файлов и возвращает словарь, где:
        ключ — ФИО, значение — данные о хобби (список строковых переменных)
    :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
    :return: Dict(str: Union[List[str]|None])
    и тут три кавычки
    # Ваш код пишите здесь

    return  # верните словарь, либо завершите исполнение программы кодом 1


dict_out = prepare_dataset('users.csv', 'hobby.csv')
with open('task_6_3_result.json', 'w', encoding='utf-8') as fw:
    json.dump(dict_out, fw, ensure_ascii=False, indent=2)
"""

import sys
import json


def prepare_dataset(path_users_file: str, path_hobby_file: str) -> dict:
    """
    Считывает данные из файлов и возвращает словарь, где:
        ключ — ФИО, значение — данные о хобби (список строковых переменных)
    :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
    :return: Dict(str: Union[List[str]|None])
    """

    with open('users.csv', 'r', encoding='utf-8') as hr:
        users = hr.read().split('\n') #.strip('\n') # .replace(',', ' ') <- если захочется убрать запятые

    with open('hobby.csv', 'r', encoding='utf-8') as hr:
        hobbys = hr.read().split('\n') # создаем list со строковыми значениями, разделенными запятой
        hobbys = [hobby.split(',') for hobby in hobbys] # list содержащий list с хобби

    result = {}
    i = 0
    if len(users) >= len(hobbys):
        while i < len(hobbys):
            result.setdefault(users[i], hobbys[i])
            i += 1
        while i < len(users):
            result.setdefault(users[i], None)
            i += 1
    else:
        exit(1)

    return result # верните словарь, либо завершите исполнение программы кодом 1


dict_out = prepare_dataset('users.csv', 'hobby.csv')
with open('task_6_3_result.json', 'w', encoding='utf-8') as fw:
    json.dump(dict_out, fw, ensure_ascii=False, indent=2)
