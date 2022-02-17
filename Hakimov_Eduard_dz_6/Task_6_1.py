from pprint import pprint


def get_parse_attrs(line: str) -> tuple:
    """Парсит строку на атрибуты и возвращает кортеж атрибутов (<remote_addr>, <request_type>, <requested_resource>)"""

    line = line.split(' ')
    save_line = line[0], line[5], line[6]

    return save_line


list_out = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    pass  # передавайте данные в функцию и наполняйте список list_out кортежами

print(list_out)

list_out = list()
with open('hello_2.txt', 'r', encoding='utf-8') as fr1:
    for line in fr1:
        list_out.append(get_parse_attrs(line))

print(list_out)


