from functools import wraps


def val_checker(func_filter):
    def checker(func):
        @wraps(func)
        def decor(x):
            if func_filter(x):
                return func(x)
            raise ValueError(f'wrong value: {x}')
        return decor
    return checker


@val_checker(lambda x: isinstance(x, int) and x > 0)
def calc_cube(x):
    return x ** 3


if __name__ == '__main__':
    print(calc_cube(5))
    print(calc_cube('ss'))
