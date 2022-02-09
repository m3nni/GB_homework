import requests
import datetime


def currency_rates_adv(code: str, cbr_url = 'http://www.cbr.ru/scripts/XML_daily.asp'):

    if not (code, cbr_url): # Ели валюта не указана
        return None # возвращаем None
    code = code.upper() # фиксируем регистр
    response = requests.get(cbr_url) # делаем первый запрос
    if response.ok:
        cur = response.text.split(code)
        if cur == 1:
            return None

        value = cur[1].split('</Value')[0].split('<Value>')[1] # получаем значение типа str
        value = float(value.replace(',', '.')) # преобразуем str во float
        # value = float('{0:.2f}'.format(value)) # ограничиваем количество знаков
        nominal = int(cur[1].split('</Nominal')[0].split('<Nominal>')[1]) # получаем номинал валюты
        kurs = value / nominal # получаем цену 1 купона (в рублях)
        kurs = float('{0:.3f}'.format(kurs))

        date_value = response.headers['Date'] # получаем Date из headers
        format = '%a, %d %b %Y %H:%M:%S GMT' # собираем формат даты
        date_value = datetime.datetime.strptime(date_value, format).date()  # обрабатываем

    return kurs, date_value


if __name__ == '__main__':
    print('Welcome')
