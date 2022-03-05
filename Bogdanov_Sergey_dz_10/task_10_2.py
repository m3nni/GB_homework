from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, value: float):
        self.size = value
        self.height = value

    @abstractmethod
    def calculate(self):
        pass


class Coat(Clothes):

    @property
    def calculate(self):
        return '{0:.2f}'.format(self.size / 6.5 + 0.5)  # для пальто (`size / 6.5 + 0.5`)


class Costume(Clothes):

    @property
    def calculate(self):
        return '{0:.2f}'.format(2 * self.height + 0.3)  # для костюма (`2 * height + 0.3`)


if __name__ == '__main__':
    coat = Coat(45.0)
    costume = Costume(3)


    print(coat.calculate)  # 7.42
    print(costume.calculate)  # 6.3
