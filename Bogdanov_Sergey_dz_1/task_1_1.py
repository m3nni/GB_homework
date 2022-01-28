"""
Реализовать вывод информации о промежутке времени в зависимости от его продолжительности
duration в секундах:

до минуты: <s> сек;
до часа: <m> мин <s> сек;
до суток: <h> час <m> мин <s> сек;
в остальных случаях: <d> дн <h> час <m> мин <s> сек.
Примеры:

> duration = 53
53 сек

> duration = 153
2 мин 33 сек

> duration = 4153
1 час 9 мин 13 сек

> duration = 400153
4 дн 15 час 9 мин 13 сек
"""

def convert_time(duration: int) -> str:
    rest_second = duration % 60 # определяем остаток секунд
    minutes = duration // 60 # определяем минуты
    hours = 0
    days = 0
    result = 0
    if minutes > 60:
        hours = minutes // 60 # определяем количество часов
        minutes = minutes % 60 # переопределяем количество минут (остаток от часов)
        if hours > 24:
            days = hours // 24 # определяем количество дней
            hours = hours % 24 # переопределяем количество часов (остаток от дней)

    # дальше определяем порядок вывода result_time в зависимости от duration
    if days < 1 and hours < 1 and minutes < 1 and rest_second >=1:
        result = (f'{rest_second} сек')
    elif days < 1 and hours < 1 and minutes >= 1:
        result = (f'{minutes} мин {rest_second} сек')
    elif days < 1 and hours >= 1 and minutes >= 0:
        result = (f'{hours} час {minutes} мин {rest_second} сек')
    elif days >=1 and hours >= 0 and minutes >= 0:
        result = (f'{days} дн {hours} час {minutes} мин {rest_second} сек')

    return result

duration = 400153
# Можно оформить в виде запроса данных у пользователя
# duration = input('Введите количество секунд (целое число): ')
result = convert_time(duration)
print(f'Путём конвертации введенного количества секунд мы получим следующий формат даты: \n {result}')

print('\n-=The end=-')