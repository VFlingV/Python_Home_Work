import random
from random import randrange, randint, choice
def get_jokes(count: int, rep = False) -> list:
    """Возвращает список шуток в количестве count"""
    # пишите реализацию своей программы здесь
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    list_out =[]
    for i in range(count):
        if rep:
            list_rand = list(map(lambda x: x.pop(random.randrange(len(x))), [nouns, adverbs, adjectives])) # долго писал данную функцию. lambda тяжело далась
        else:
            list_rand = list(map(random.choice, [nouns, adverbs, adjectives]))
        list_out.append(' '.join(list_rand))
    return list_out


print(get_jokes(6, False))
print(get_jokes(3, True))
# в основном были сложности в освоеннии lambda/map/filter

