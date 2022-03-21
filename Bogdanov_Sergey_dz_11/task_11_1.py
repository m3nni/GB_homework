class Date:
    __date: str

    def __init__(self, date: str):
        self.__date = date

    @classmethod
    def split_to_numb(cls, date: str):
        try:
            return(list(map(int, date.split('-'))))
        except:
            raise ValueError('Проверьте введенную дату.')

    @staticmethod
    def is_valid(date: str):

        day: int
        month: int
        year: int

        try:
            day, month, year = Date.split_to_numb(date)
        except:
            return False

        if not 1 <= month <= 12:
            return False

        if not 0 <= year:
            return False

        if not 1 <= day <= 31:
            return False

        if month in [4, 6, 9, 11] and day == 31:
            return False

        if (month == 2 and day == 29 and year % 4 != 0 and year % 100 != 0 and year % 400 != 0):
            return False

        return True


if __name__ == '__main__':
    test_date = Date('22-03-2022')
    Date.split_to_numb('22-03-2022')
    # тут выскочит исключение
    # Date.split_to_numb('22-03-202F')
    test_date.is_valid('22-03-2022')
