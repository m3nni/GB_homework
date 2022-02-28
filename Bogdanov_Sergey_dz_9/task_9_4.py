class Car:
    is_police: bool = False

    def __init__(self, speed: int, color: str, name: str):
        """
        Конструктор класса
        :param speed: текущая скорость автомобиля
        :param color: цвет автомобиля
        :param name: название марки автомобиля
        """
        self.speed = speed
        self.color = color
        self.name = name

    def go(self) -> None:
        """
        Увеличивает значение скорости на 15
        :return: в stdout сообщение по формату
            'Машина <название марки машины> повысила скорость на 15: <текущая скорость машины>'
        """
        self.speed += 15
        print(f'Машина {self.name} повысила скорость на 15: {self.speed}')

    def stop(self) -> None:
        """
        При вызове метода скорость становится равной '0'
        :return: в stdout сообщение по формату '<название марки машины>: остановилась'
        """
        self.speed = 0
        print(f'{self.name}: остановилась')

    def turn(self, direction: str) -> None:
        """
        Принимает направление движения автомобиля
        :param direction: строковое представление направления движения, может принимать только
            следующие значения: 'направо', 'налево', 'прямо', 'назад'
        :return: в stdout сообщение по формату
            '<название марки машины>: движется <direction>'
        """
        variable = 'направо', 'налево', 'прямо', 'назад'
        self.direction = direction
        if variable.count(self.direction) == 1:
            print(f'{self.name}({self.__class__.__name__}): движется {self.direction}')
        else:
            raise ValueError('нераспознанное направление движения')

    def show_speed(self) -> None:
        """
        Проверка текущей скорости автомобиля
        :return: в stdout выводит сообщение формата
            '<название марки машины>: текущая скорость <значение текущей скорости> км/час'
        """
        print(f'{self.name}: текущая скорость {self.speed} км/час')


class TownCar(Car):

    def show_speed(self) -> None:
        """
        Проверка текущей скорости автомобиля
        :return: в stdout выводит сообщение формата
            '<название марки машины>: текущая скорость <значение текущей скорости> км/час'
        """
        if self.speed > 60:
            print('Alarm!!! Speed!!!')
        elif self.speed <= 60:
            print(f'{self.name}: текущая скорость {self.speed} км/час')


class WorkCar(Car):

    def show_speed(self) -> None:
        """
        Проверка текущей скорости автомобиля
        :return: в stdout выводит сообщение формата
            '<название марки машины>: текущая скорость <значение текущей скорости> км/час'
        """
        if self.speed > 40:
            print('Alarm!!! Speed!!!')
        elif self.speed <= 40:
            print(f'{self.name}: текущая скорость {self.speed} км/час')


class SportCar(Car):
    pass

class PoliceCar(Car):
    is_police: bool = True

    def show_speed(self) -> None:
        """
        Проверка текущей скорости автомобиля
        :return: в stdout выводит сообщение формата
            '<название марки машины>: текущая скорость <значение текущей скорости> км/час'
        """
        if self.is_police:
            print(f'{self.name}: текущая скорость {self.speed} км/час')
            print('Вруби мигалку и забудь про скорость!')
        elif not self.is_police:
            print(f'{self.name}: текущая скорость {self.speed} км/час')


if __name__ == '__main__':
    town_car = TownCar(41, "red", 'WW_Golf')
    work_car = WorkCar(41, 'yellow', 'BobCat')
    police_car = PoliceCar(120, "blue", 'BMW')
    sport_car = SportCar(300, 'white', 'Ferrari')
    print(f'Городской автомобиль: {town_car.speed}, {town_car.color}, {town_car.name}')
    print(f'Рабочий автомобиль: {work_car.speed}, {work_car.color}, {work_car.name}')
    print(f'Полицейский автомобиль: {police_car.speed}, {police_car.color}, {police_car.name}')
    print(f'Спортивный автомобиль: {sport_car.speed}, {sport_car.color}, {sport_car.name}')
    town_car.go()  # Машина WW_Golf повысила скорость на 15: 56
    town_car.show_speed()  # WW_Golf: текущая скорость 56 км/час
    work_car.show_speed()  # Alarm!!! Speed!!!
    town_car.stop()  # WW_Golf: остановилась
    police_car.show_speed()
    # BMW: текущая скорость 120 км/час
    # Вруби мигалку и забудь про скорость!
    sport_car.turn('назад')  # Ferrari(SportCar): движется назад
    #sport_car.turn('right')
    """
    Traceback (most recent call last):
      ...
    ValueError: нераспознанное направление движения
    """