"""
Задание 5 **(вместо 4)
Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было задать имя обоих
исходных файлов и имя выходного файла. Проверить работу скрипта.
"""

import sys


def prepare_dataset(path_users_file: str, path_hobby_file: str, *args):
    """
    Считывает данные из файлов и сохраняет объединенные данные в файл users_hobby.txt,
        где хобби пишется через двоеточие и пробел после ФИО.
    :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
    :return: users_hobby.txt
    """

    users = []
    with open(path_users_file, 'r', encoding='utf-8') as hr:
        while True:
            u_line = hr.readline().strip('\n') # .replace(',', ' ') <- если захочется убрать запятые
            if not u_line:
                break
            users.append(u_line)
    hobbys = []
    with open(path_hobby_file, 'r', encoding='utf-8') as hr:
        while True:
            h_line = hr.readline().strip('\n')
            if not h_line:
                break
            hobbys.append(h_line)

    result = ''
    i = 0
    if len(users) >= len(hobbys):
        while i < len(hobbys):
            result += f"{users[i]}: {hobbys[i]}\n"
            i += 1
        while i < len(users):
            result += f"{users[i]}: {None}\n"
            i += 1
    else:
        exit(1)
    while i < len(users):
        result += f"{users[i]}: {hobbys[i]}\n"
        i += 1
    return result

result_file = sys.argv[3]
result = prepare_dataset('users.csv', 'hobby.csv')
with open(result_file, 'w', encoding='utf-8') as fw:
    fw.write(result)

if __name__ == '__main__':

    user = sys.argv[1]
    hobbys = sys.argv[2]
    prepare_dataset(user, hobbys, result_file)
