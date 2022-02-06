#  Задание 5
#  Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):
#
#  nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
#  adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
#  adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#  Например:
#
#  >>> get_jokes(2)
#  ["лес завтра зеленый", "город вчера веселый"]
#  Документировать код функции.
#
#  Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках (когда каждое слово можно использовать только в одной шутке)?
#  Сможете ли вы сделать аргументы именованными?
#  ВНИМАНИЕ! Используйте стартовый код для своей реализации:
#
#  nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
#  adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
#  adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#
#
#  def get_jokes(count: int) -> list:
#      """Возвращает список шуток в количестве count"""
#      # пишите реализацию своей программы здесь
#      list_out = ["здесь собранные шутки"]
#      return list_out
#
#
#  print(get_jokes(2))
#  print(get_jokes(10))
#
#
#  # Раскомментируйте для реализации подзаданий: документирование, флаг и именованные аргументы
#  # def get_jokes_adv(...) -> list:
#  #     # пишите реализацию здесь
#  #     return []

from random import randint, choice, randrange

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера",  "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(count: int) -> list:
    """Возвращает список шуток в количестве count"""
    indx = 0 # задаём начальный индекс для последующего отсчёта количества шуток
    list_out = []  # ["здесь собранные шутки"]
    while indx < count: # до тех пор, пока индекс меньше желаемого количества шуток
        joke = f'{choice(nouns)}, {choice(adverbs)}, {choice(adjectives)}' # собираем шутку из случайных значений (по 1 из каждого списка)
        list_out.append(joke)
        indx += 1
    return list_out


print(get_jokes(2))
print(get_jokes(10))

# Раскомментируйте для реализации подзаданий: документирование, флаг и именованные аргументы
def get_jokes_adv(count_joke: int = 1, repeat: bool = True, **kwargs) -> list: #repeat: int = 1
    """
    Возвращает "шутки" в количестве загаданных (int).
    
    :param count_joke: int - количество желаемых "шуток";
    :param repeat: bool  - разрешить повтор: True, запретить повтор: repeat False;
    :return: list_out[] список строковых элементов
    """
    # делаем копии фраз (чтобы не "убить" оригинал)
    copy_nouns = nouns
    copy_adverbs = adverbs
    copy_adjectives = adjectives
    list_out = []  # ["здесь собранные шутки"]
    indx = 0 # устанавливае начальное значение

    if len(nouns) <= len(adverbs) < len(adjectives): # отбираем нужную длину списка (на случай, если они разной длины)
        num_jokes = len(nouns)
    elif len(adverbs) <= len(nouns) < len(adjectives):
        num_jokes = len(adverbs)
    else:
        num_jokes = len(adjectives)

    if repeat: # Если повторение слов разрешено
        while indx < count_joke:
            list_out.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')  # собираем шутку из случайных значений (по 1 из каждого списка)
            indx += 1
    elif not repeat: # Если повторение слов запрещено
        if num_jokes >= count_joke: # Если длина списка больше(равна) количеству желаемых шуток
            while indx < count_joke: # пока индекс меньше количества желаемых шуток
                # выводим нужное количество фраз
                list_out.append(f'{copy_nouns.pop(randrange(0, num_jokes))} {copy_adverbs.pop(randrange(0, num_jokes))} {copy_adjectives.pop(randrange(0, num_jokes))}')
                num_jokes -= 1
                indx += 1
        else:
            list_out.append(f'Увы, у нас не хватит слов на столько шуток. Максимум можно сочинить: {num_jokes} разных шуток.')
    return list_out


print(get_jokes_adv(3))
print(get_jokes_adv(6, False))
