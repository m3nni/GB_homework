import sys


def add_sale(price: str) -> float:

    price = price.replace(',', '.')
    try:
        price = float(price)
    except:
        print('Поддерживается ввод значений в форматах: 21.05 / 21,05 / 21')

    if type(price) == float:
        with open('bakery.csv', 'a', encoding='utf-8') as fw:
            fw.write(f'{price}\n')


if __name__ == '__main__':

    try:
        add_sale(sys.argv[1])
    except:
        print('Введите стоимость товара (например: 21.05)')
