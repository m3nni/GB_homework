class Complex:

    def __init__(self, real: float, img: float):

        if isinstance(real, int) or isinstance(real, float):
            self.real = real
        else:
            raise ValueError('Неверный тип (нужен int или float)')

        if isinstance(img, int) or isinstance(img, float):
            self.img = img
        else:
            raise ValueError('Неверный тип (нужен int или float)')


    def __str__(self) -> str:
        return f"{self.real}{' + ' if self.img >= 0 else ' - ' }{abs(self.img)}j"

    def __add__(self, other):
        return f"{self.real + other.real}{' + ' if (self.img + other.img) >= 0 else ' - ' }{abs(self.img + other.img)}j"

    def __mul__(self, other):
            return Complex(
                real=self.real * other.real - self.img * other.img,
                img=self.real * other.img + other.img * other.real
                )

if __name__ == '__main__':
    number1 = Complex(1, 3)
    number2 = Complex(4, 3)

    print(number1)  # 1 + 3j
    print(number2)  # 4 + 3j
    print(number1 + number2)  # 5 + 6j
    print(number1 * number2)  # -5 + 15j

    """
    Через Python Console:
    x = complex(1, 3)
    y = complex(4, 3)
    
    print(x + y) -> (5+6j)
    
    print(x * y) -> (-5+15j)
    """

