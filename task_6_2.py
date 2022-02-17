"""
Задание 2 *(вместо 1)
Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.

Примечание: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами,
размер которых превышает объем ОЗУ компьютера.
"""

def get_parse_attrs(line: str) -> tuple:

    addr_tuple = line.split()[0]
    return addr_tuple


addr_list = [] # парсим строки, собираем адреса
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    while True:
        line = fr.readline()
        if not line:
            break
        addr_list.append(get_parse_attrs(line))

uniq_addrs = set(addr_list) # собираем уникальные адреса
uniq_addrs_count = {} # дальше вычисляем, какой адрес сколько раз встречается (собираем словарь key=ip, value= количество count)
while len(uniq_addrs) != 0: # ну тут понятно
    value = uniq_addrs.pop() # берем значение из множества уникальных адресов
    count_value = str(addr_list.count(value)) # смотрим, сколько раз он встречается в исходном списке
    uniq_addrs_count[f'{value}'] = count_value # собираем пару для словаря

sort_uac = sorted(uniq_addrs_count.items(), key=lambda x: x[1]) # сортируем, сортируем да не высортируем
winner = sort_uac.pop() # получаем адрес спамера
print(f'Спамер стучался вот от сюда {winner[0]} аж целых {winner[1]} раз.') # выводим результат
