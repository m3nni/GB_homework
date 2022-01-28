"""
a) Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):

Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.

Например, число `19 ^ 3 = 6859` будем включать в сумму, так как `6 + 8 + 5 + 9 = 28` – делится
нацело на `7`.
Внимание: использовать только арифметические операции!

b) К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
сумма цифр которых делится нацело на 7.

*c) Решить задачу под пунктом b, не создавая новый список. (если будете решать - либо
создайте доп. функцию, либо перепишите существующую sum_list_2)
"""

def sum_list_1(dataset: list) -> int:
    """Вычисляет сумму чисел списка dataset, сумма цифр которых делится нацело на 7"""
    sum_del_7 = [] # создаем пустой список
    for i in range(len(dataset)):
        sum_elements = 0
        num = dataset[i]
        while num != 0:
            sum_elements = sum_elements + num % 10
            num = num // 10
        if sum_elements % 7 == 0:
            sum_del_7.append(dataset[i])
    total = 0
    for number in sum_del_7:
        total += number
    return total

def sum_list_2(dataset: list) -> int:
    """К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка,
        сумма цифр которых делится нацело на 7"""
    sum_del_7_plus_17 = 0
    for i in range(len(dataset)):
        dataset[i] = dataset[i] + 17
    for i in range(len(dataset)):
        sum_elements = 0
        num = dataset[i]
        while num != 0:
            sum_elements = sum_elements + num % 10
            num = num // 10
        if sum_elements % 7 == 0:
            sum_del_7_plus_17 = sum_del_7_plus_17 + dataset[i]
    return sum_del_7_plus_17

my_list = []
for i in range (1, 1001, 2):
    cube = i ** 3
    my_list.append(cube)

result_1 = sum_list_1(my_list)
print('Результат работы функции № 1 (sum_list_1): ', result_1)
result_2 = sum_list_2(my_list)
print('Результат работы функции № 2 (sum_list_2): ', result_2)

print('\n-=The end=-')
