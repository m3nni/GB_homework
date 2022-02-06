# Задание 4
# *(вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки
# в формате «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий,
# а значения — словари, реализованные по схеме предыдущего задания и содержащие записи,
# в которых фамилия начинается с соответствующей буквы.
#
# Например:
#
# >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# {
#     "А": {
#         "П": ["Петр Алексеев"]
#     },
#     "И": {
#         "И": ["Илья Иванов"]
#     },
#     "С": {
#         "И": ["Иван Сергеев", "Инна Серова"],
#         "А": ["Анна Савельева"]
#     }
# }
# Как поступить, если потребуется сортировка по ключам?

def thesaurus_adv(*args) -> dict:
    dict_out = {}

    dict_second_name = {} # словарь, сортированный по фамилии
    for person_2 in args:  # собираем список по фамилиям
        future_key_2 = person_2.find(' ') + 1 # находим индекс первой буквы после пробела
        if dict_second_name.get(person_2[future_key_2]) == None:
            dict_second_name[person_2[future_key_2]] = [person_2]
        else:
            dict_second_name[person_2[future_key_2]] += [person_2]

    """
    Следующий блок был изначально добавлен, но после я посчитал его излишним. Пусть останется на память.
    #print('dict_second_name', dict_second_name)
    dict_first_name = {}  # словарь, сортированный по имени
    for person in args: #собираем список из первого задания (по букве имени)
        future_key = str(person[0])
        if dict_first_name.get(future_key) == None:
            dict_first_name[future_key] = [person]
        else:
            dict_first_name[future_key] += [person]
    print('dict_first_name', dict_first_name)
    """

    # сортируем дальше (значения сортируем по имени).
    dict_len = len(dict_second_name)
    for i in range(dict_len):
        a = list(dict_second_name.popitem())
        item_1 = a[0]
        item_2 = a[1]
        item_dict = {}
        for i in item_2:
            key = str(i[0])
            if item_dict.get(key) == None:
                item_dict[key] = [i]
            else:
                item_dict[key] += [i]
        dict_out[item_1] = item_dict
    print(dict_out)
    return dict_out


#print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Чебурек Чебуреков", "Петруха Сергеев", "Шыпа Ципович", "Илья Петрович", "Никола Басков"))
our_dict = thesaurus_adv("Инна Серова", "Иван Сергеев",  "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Чебурек Чебуреков", "Петруха Сергеев", "Шыпа Ципович", "Илья Петрович", "Никола Басков")

our_dict_tuple = sorted(our_dict.items(), key=lambda x: x[0]) # разбиваем словарь на кортежи и сортируем по первому значению (по ключам)
out_dict_sorted = dict(our_dict_tuple) # собираем кортежи обратно в словарь
print(out_dict_sorted)
