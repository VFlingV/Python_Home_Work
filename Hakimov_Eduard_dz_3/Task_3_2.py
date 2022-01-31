def num_translate_adv(value: str) -> str:
    """переводит числительное с английского на русский """
    # реализуйте здесь, где хранить необходимые исходные данные определитесь самостоятельно
    notepad = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять',
    }
    if value.istitle():
        value = value.lower()
        str_out = notepad.get(value).title()
    else:
        str_out = notepad.get(value)
    return str_out


print(num_translate_adv("One"))
print(num_translate_adv("two"))
