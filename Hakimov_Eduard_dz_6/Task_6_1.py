from pprint import pprint


def get_parse_attrs(line: str) -> tuple:
    """Парсит строку на атрибуты и возвращает кортеж атрибутов (<remote_addr>, <request_type>, <requested_resource>)"""
    line = line.split(' ')
    ip = line[0]
    ptp = line[5]
    php = line[6]
    line_save = ip, ptp, php

    return line_save


list_out = list()
with open('test.txt', 'r', encoding='utf-8') as fr:
    for line in fr:
        list_out.append(get_parse_attrs(line))

pprint(list_out)