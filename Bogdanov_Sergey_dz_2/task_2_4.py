# Задание 4
# На вход будет подаваться список, содержащий искажённые данные с должностями и именами сотрудников:
#
# ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
# 'директор аэлита']
# Известно, что имя сотрудника всегда в конце строки!
#
# Обработать все элементы списка и вернуть в качестве результата список, состоящий из фраз вида:
#
# ['Привет, Игорь!', 'Привет, Марина!', 'Привет, Николай!', 'Привет, Аэлита!']

# Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду.
#
# Можно ли при этом не создавать новый список?
#
# ВНИМАНИЕ! Используйте стартовый код для своей реализации:
#
# def convert_name_extract(list_in: list) -> list:
#     """Извлекает имена из элементов и формирует список приветствий."""
#     # пишите реализацию своей программы здесь
#     list_out = ["здесь должены оказаться результирующие строковые приветствия"]
#     return list_out
#
#
# my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# result = convert_name_extract(my_list)
# print(result)

# ----------------------------------------------------------------------------------------------------------------------

def convert_name_extract(list_in: list) -> list:
    """Извлекает имена из элементов и формирует список приветствий."""
    list_out = []
    for i in range(len(list_in)):
        get_first_person = list_in.pop()  # забираем последний индекс из списка list_in
        # print(get_first_person, type(get_first_person))
        first_item_split = get_first_person.split()  # делаем сплит get_first_person, получаем новый список first_item_split
        # print(get_item_2, type(get_item_2))
        get_position = ' '.join(first_item_split[0:-1:1]).lower()  # получаем должность с помощью среза, приводим к нижнему регистру
        # print(get_position, type(get_position))
        get_name = first_item_split.pop().lower().capitalize()  # забираем имя и приводим его к нижнему регистру и "поднимаем" первую букву
        # print(get_name, type(get_name))
        new_person = ' '.join([get_position, get_name])  # в новый список заносим дожность и имя сотрудника
        # print(new_item, type(new_item))
        list_out.insert(0, new_person)  # добавляем итем в список list_out
    #list_out = ["здесь должены оказаться результирующие строковые приветствия"]
    return list_out

my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
print(f'Входящий список: {my_list}')
result = convert_name_extract(my_list)
print(f'Обработанный список: {result}')