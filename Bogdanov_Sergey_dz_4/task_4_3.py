"""
*(вместо 2) В task_4_3.py создать функцию currency_rates_adv() аналогичную currency_rates() прошлого задания, только теперь она должна возвращать кроме курса ещё и дату, которая передаётся в ответе сервера.

Дата должна быть в виде объекта date. Т.е. функция должна возвращать кортеж из двух элементов следующих типов float и datetime.date

Подумайте, как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?

ВНИМАНИЕ! Используйте стартовый код для своей реализации:

import datetime

def currency_rates_adv(code: str):
    # ваша реализация здесь
    ...

kurs, date_value = currency_rates_adv("USD")

empty = bool(not kurs and not date_value)
if not empty and not isinstance(kurs, float):
    raise TypeError("Неверный тип данных у курса")
if not empty and not isinstance(date_value, datetime.date):
    raise TypeError("Неверный тип данных у даты")
print(kurs, date_value)
"""