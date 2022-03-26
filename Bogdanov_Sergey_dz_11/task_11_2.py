class ZeroDiv(Exception):

    def __init__(self, *args: object):
        super().__init__(*args)


if __name__ == '__main__':

    from sys import exit

    first = 0
    second = 0

    try:
        first = float(input('Введите первое число: '))
        second = float(input('Введите второе число: '))
    except:
        print('Неверный ввод. Проверьте введенное число.')
        exit(1)

    try:
        if second == 0:
            raise ZeroDiv('На 0 делить нельзя.')
        print(f'{first}/{second} = {first/second}')
    except ZeroDiv as exept:
        print(exept)
