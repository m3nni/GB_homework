class AllNumbers(Exception):

    def __init__(self, *args: object):
        super().__init__(*args)


if __name__ == "__main__":

    func_list = []
    while True:
        try:
            value = input('Вводите значение (для завершения программы введите "stop"): ')
            if value == "stop":
                break
            elif not value.isdigit():
                raise AllNumbers()
            else:
                func_list.append(int(value))
        except AllNumbers:
            print('Вводите только числа!')

    print(*func_list)
