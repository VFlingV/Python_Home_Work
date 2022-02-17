import re


def email_parse(email: str) -> dict:
    """
    Парсит переданную email-строку на атрибуты и возвращает словарь
    :param email: строковое входное значение обрабатываемого email
    :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
    """
    RE_MAIL = re.compile(r'(?P<username>[A-Za-z0-9\.\-\_]+)@(?P<domain>[a-zA-Z0-9\.\-\_]+)')
    if not RE_MAIL.match(email):
        raise ValueError(f'err email: {email}')
    result = map(lambda x: x.groupdict(), RE_MAIL.finditer(email))
    print(result.__next__())
    #print(RE_MAIL.match(email).groupdict())


#if __name__ == '__main__':
#    email_parse('someone@geekbrains.ru')
#    email_parse('someone@geekbrainsru')
for i in ['someone@geekbrains.ru', 'someone@geekbrainsru']:
    try:
        email_parse(i)
    except ValueError as err:
        print(err)