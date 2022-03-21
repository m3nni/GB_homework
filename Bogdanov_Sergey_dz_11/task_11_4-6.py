from abc import ABC


class ValueError(Exception):
    pass


class Warehouse(ABC):

    what_we_have: dict = {'Принтер': 0,
                          'Сканер': 0,
                          'Ксерокс': 0
                          }

    @classmethod
    def add_equip(cls, what_is, value: int = 1):
        if isinstance(value, int) and value >= 1 and cls.what_we_have.get(what_is._type) >= 0:
            cls.what_we_have[what_is._type] += value
            print(f'На склад добавлен {what_is._type} ({value} шт). Теперь их: {cls.what_we_have.get(what_is._type)}')
        else:
            raise ValueError('Неверное значение')

    @classmethod
    def remove_equip(cls, what_is, value: int = 1, company_name: str = 'Noname'):

        if isinstance(value, int):
            if cls.what_we_have.get(what_is._type) > 0:
                cls.what_we_have[what_is._type] -= value
                print(f'Со склада отгрузили {what_is._type} ({value} шт) для компании "{company_name}". Остаток на складе: {cls.what_we_have.get(what_is._type)}')
            else:
                print(f'Что там надо? Ах, {what_is._type}! ')
                print(f'Увы, {what_is._type} на складе отсутствует.')
        else:
            raise ValueError('Неверное значение')


class OfficeEquipment(ABC):
    paper_size: str = 'A4'

    def __init__(self, create_by: str = None, made_in: str = None):
        self.create_by = create_by
        self.made_in = made_in


class Printer(OfficeEquipment):
    ink: bool = False
    _type: str = 'Принтер'


class Scanner(OfficeEquipment):
    scan_resolution: str = '1200x780'
    _type: str = 'Сканер'


class Copier(OfficeEquipment):
    page_to_copy: int = 1
    _type: str = 'Ксерокс'


if __name__ == '__main__':

    printer1 = Printer('HP', 'China')
    Warehouse.add_equip(printer1)
    print(Warehouse.what_we_have)
    Warehouse.add_equip(Printer('HP', 'China'), 3)
    print(Warehouse.what_we_have)
    Warehouse.remove_equip(printer1)
    Warehouse.remove_equip(printer1, 2, 'Чиполино')
    print(Warehouse.what_we_have)
    Warehouse.remove_equip(Scanner())
    Warehouse.add_equip(Scanner('Lo'), 3)

    # Если раскомитить, выдаст ошибку
    # Warehouse.remove_equip(Scanner(), 'вы')

    # Если раскомитить, выдаст ошибку
    # Warehouse.add_equip(Scanner, -2)
    # Warehouse.add_equip(Scanner, 'asdf')
