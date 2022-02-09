import requests


def currency_rates(code: str, cbr_url='http://www.cbr.ru/scripts/XML_daily.asp') -> float:

    if not (code, cbr_url): # Ели валюта не указана
        return None # возвращаем None

    code = code.upper() # фиксируем регистр
    response = requests.get(cbr_url) # делаем первый запрос
    if response.ok:
        cur = response.text.split(code)
        if len(cur) == 1:
            return None

        value = cur[1].split('</Value')[0].split('<Value>')[1] # получаем значение типа str
        value = float(value.replace(',', '.')) # преобразуем str во float
        value = float('{0:.2f}'.format(value)) # ограничиваем количество знаков
        nominal = int(cur[1].split('</Nominal')[0].split('<Nominal>')[1]) # получаем номинал валюты
        result_value = value / nominal # получаем цену 1 купюры (в рублях)

    return result_value


print(currency_rates('USD'))
print(currency_rates('EUR'))
print(currency_rates('some_else'))
