# *(вместо задачи 1) Перепишите функцию из задания 1 изменив название
# на num_translate_adv(): реализовать корректную работу с числительными,
# начинающимися с заглавной буквы — результат тоже должен быть с заглавной.
#
# Например:
#
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

# 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find',
# 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit',
# 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper',
# 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind',
# 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith',
# 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'
def num_translate_adv(value: str) -> str:
    """переводит числительное с английского на русский """

    numbers = {'zero': 'ноль', 'one': 'один', 'two': 'два',
               'three': 'три', 'four': 'четыре', 'five': 'пять',
               'six': 'шесть', 'seven': 'семь', 'eight': 'восемь',
               'nine': 'девять'
               }

    if value[0].istitle():
        str_out = numbers.get(value.lower(), 'Кажется вы ошиблись в написании цифры. Попробуйте ещё раз.').capitalize()
    else:
        str_out = numbers.get(value.lower(), 'Кажется вы ошиблись в написании цифры. Попробуйте ещё раз.')
    return str_out


print(num_translate_adv("One"))
print(num_translate_adv("oNe"))
print(num_translate_adv("onE"))
print(num_translate_adv("sEVEn"))
print(num_translate_adv("FIve"))
print(num_translate_adv("sIX"))
print(num_translate_adv("SevEN"))
print(num_translate_adv("eiGHt"))
print(num_translate_adv("NINE"))
print(num_translate_adv("ZerO"))
