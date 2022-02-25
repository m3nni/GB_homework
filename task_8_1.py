import re

def email_parse(email: str) -> dict:
    """
    Парсит переданную email-строку на атрибуты и возвращает словарь
    :param email: строковое входное значение обрабатываемого email
    :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
    """
    
    RE_MAIL = re.compile(r'(?P<name>[\w\d._]+)@(?P<domain>[a-zA-Z0-9_-]+\.\w+)')
    good_email = re.match(RE_MAIL, email)
    if not good_email:
        raise ValueError(f'wrong email: {email}')
    dict_out = good_email.groupdict()
    return dict_out


if __name__ == '__main__':
    print(email_parse('someone@geekbrains.ru'))
    #print(email_parse('someone@geekbrainsru'))
    print(email_parse('bsv.0042@gmail.ru'))
    print(email_parse('__logger._23@mail.ru'))
