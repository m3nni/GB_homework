"""
Задание 3
*(вместо задачи 2) Решить задачу 2, не создавая новый список (как говорят, in place).
Эта задача намного серьёзнее, чем может сначала показаться.
"""

# ----------------------------------------------------------------------------------------------------------------------

def convert_list_in_str(list_in: list) -> str:
    """Обособляет каждое целое число кавычками, добавляя кавычку до и после элемента
        списка, являющегося числом, и дополняет нулём до двух целочисленных разрядов.
        Формирует из списка результирующую строковую переменную и возвращает."""
    str_out = ''
    len_list = len(list_in)
    indx = 0
    while indx != len_list:
        first = list_in.pop(0)
        if first.isalpha():  # если значение БУКВА
            str_out += first + ' '
        if first.isdigit():  # если значение состоит из ЦИФР
            if len(first) <= 1:  # Если длина ЧИСЛА (количество цифр меньше или равно 1)
                str_num = list(first)  # делаем из строки список
                str_num.insert(0, '0')  # на индекс 0 вставляем значение "0"
                str_num = ''.join(str_num)  # собираем строку из списка
                str_out += '"' + str_num + '"' + ' '
            else:
                str_out += '"' +first + '"' + ' '
        if not first.isdigit() and not first.isalpha():  # Если не чистые цифры, и не чистые буквы
            list_i = list(first)  # по аналогии -> разбиваем строку и создаем список
            str_i = []  # пустой список из которого будем делать нужную строку
            for i in list_i:
                if i.isdigit() and len(list_i) <= 2:
                    str_i.append(i)
                elif not i.isdigit() and len(list_i) <= 2:
                    str_i.append(i)
                    str_i.append('0')
                else:
                    str_i.append(i)
            str_i = ''.join(str_i)  # собираем итоговую строку
            str_out += '"' + str_i + '"' + ' '
        indx = indx + 1
    return str_out


my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = convert_list_in_str(my_list)
print(result)
