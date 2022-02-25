"""
Задание 2 *(вместо 1)
Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
для получения информации вида: (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>,
<response_code>, <response_size>), например:

raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')

Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле?
Были ли особенные строки? Можно ли для них уточнить регулярное выражение?
"""

import re
from pprint import  pprint

def nginx_parse(raws: str):

    RE_NGINX = re.compile(r'(?P<addres>^\S+)[\s-]*\[(?P<date>.*)\]\s*\"(?P<type>\S+)\s*(?P<resource>/[\w\W]+?)\s+.*\"\s+(?P<code>\d+?)\s+(?P<size>\d+)')
    parsed_raw = [re.findall(RE_NGINX, raw) for raw in raws] # вывод в список
    # parsed_raw = (re.findall(RE_NGINX, raw) for raw in raws) # вывод в генератор
    return parsed_raw

"""
raw = 93.180.71.3 - - [17/May/2015:08:05:32 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)"
parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
"""

if __name__ == '__main__':
    with open('nginx_logs.txt', 'r', encoding='utf-8') as rf:
        raws = rf.readlines()
        # print(len(raws)) # 51462
        parsed_raw = nginx_parse(raws)
        # print(len(parsed_raw)) # 51462
        pprint(parsed_raw, width=150)
