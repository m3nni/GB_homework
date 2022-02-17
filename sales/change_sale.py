import sys


def change_sale(number, new_price):

    list_a = []
    str_b = ''
    number = int(number)
    new_price = float(new_price)
    with open('bakery.csv', 'r', encoding='utf-8') as rf:
        while True:
            price = rf.readline().replace('\n', '')
            if not price:
                break
            list_a.append(price)

    list_a.insert(0, '')
    list_a.pop(number)
    list_a.insert(number, new_price)
    list_a.pop(0)

    i = 1
    for value in list_a:
        str_b += f'{value}\n'
        i += 1
    with open('bakery.csv', 'w', encoding='utf-8') as wf:
        wf.write(str_b)

#change_sale(2, 404)

if __name__ == '__main__':

    try:
        number = int(sys.argv[1])
    except:
        print('Укажите индекс цены, которую хотите заменить. (например: 3)')

    try:
        new_price = float(sys.argv[2])
    except:
        print('Укажите цену, которую надо указать. (например: 22.12)')

    change_sale(number, new_price)
