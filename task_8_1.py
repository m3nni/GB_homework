"""
Задание 1
Написать тело функцию email_parse(email: str), которая при помощи регулярного выражения извлекает
имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря.
Если адрес не валиден, выбросить исключение ValueError. Пример:

$ email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
$ email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru


ВНИМАНИЕ! Используйте стартовый код для своей реализации:

import re


def email_parse(email: str) -> dict:
    "" "
    Парсит переданную email-строку на атрибуты и возвращает словарь
    :param email: строковое входное значение обрабатываемого email
    :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
    "" "
    RE_MAIL = re.compile(r'ваше регулярное выражение')
    pass  # пишите реализацию здесь


if __name__ == '__main__':
    email_parse('someone@geekbrains.ru')
    email_parse('someone@geekbrainsru')
"""

import re

def email_parse(email: str) -> dict:
    """
    Парсит переданную email-строку на атрибуты и возвращает словарь
    :param email: строковое входное значение обрабатываемого email
    :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
    """
    
    RE_MAIL = re.compile(r'(?P<name>[\w\d._]+)@(?P<domain>[a-zA-Z0-9_-]+\.\w+)')
    good_email = re.match(RE_MAIL, email)
    if not good_email:
        raise ValueError(f'wrong email: {email}')
    dict_out = good_email.groupdict()
    return dict_out


if __name__ == '__main__':
    print(email_parse('someone@geekbrains.ru'))
    #print(email_parse('someone@geekbrainsru'))
    print(email_parse('bsv.0042@gmail.ru'))
    print(email_parse('__logger._23@mail.ru'))
