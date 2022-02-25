from functools import wraps

def type_logger(calc_cube):

    @wraps(calc_cube)
    def wrap(*args, **kwargs):

        all_args = list(args) + list(kwargs.values())
        #print(all_args)
        if len(all_args) == 1:
            print(f'{calc_cube.__name__}({all_args[0]}: {type(all_args[0])})')
        elif len(all_args) > 1:
            print(', '.join([f"{calc_cube.__name__}({x}: {type(x)})" for x in all_args]))
        # Если захочется вывести кубы всех аргументов функции calc_cube(x) -> раскомитить следующие строки:
        # result = [calc_cube(e) for e in all_args]
        # print(result)
    return wrap


@type_logger
def calc_cube(x):
   return x ** 3


if __name__ == '__main__':

    a = calc_cube(3, 2, 5.2)
    a = calc_cube(4)
