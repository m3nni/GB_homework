import sys


def show_sales(i_start = 1, i_end = 0):

    with open('bakery.csv', 'r', encoding='utf-8') as rf:

        price = rf.read().split('\n')
        if len(price) == 1:
            print('Список пуст')
        price.insert(0, price.pop()) # извлекаем последнее значение (пустое) и переносим его в начало, чтобы индекс 0 был пустым.
        i_start = int(i_start)
        i_end = int(i_end)
        i_len = len(price) - 1

        if i_start > len(price) - 1:
            print(f'Записи под номером {i_start} в базе нет.')
        elif i_end > len(price):
            print(f'Записи {i_end} нет. Крайняя запись имеет номер {i_len}.')
        elif i_start < i_end and i_end <= len(price):
            while i_start != i_end + 1:
                print(price[i_start])
                i_start += 1
        else:
            while i_start != len(price):
                print(price[i_start])
                i_start += 1


if __name__ == '__main__':

    try:
        i_start = int(sys.argv[1])
    except:
        i_start = 1

    try:
        i_end = int(sys.argv[2])
    except:
        i_end = int(0)

    show_sales(i_start, i_end)
