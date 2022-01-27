# задание 1

def convert_time(duration: int) -> str:
    # пишите реализацию своей программы здесь
    s = duration
    m = 60
    h = 3600
    d = 86400
    w = 604800
    if s < m:
        result = '{} сек'.format(s)
        # не нашел вариантов как актуально вывезти результат в нормальном формате кроме как .format
    elif m <= s and h > s:
        new_m = s //m
        new_s = s % m
        result = '{} мин {} сек'.format(new_m , new_s)
    elif s >= h and s < d:
        new_h = s // h
        s = s % h
        new_m = s // m
        new_s = s % m
        result = '{} час {} мин {} сек'.format(new_h, new_m, new_s);
    elif s >= d and s < w:
        new_d = s // d
        s = s % d
        new_h = s // h
        s = s % h
        new_m = s // m
        new_s = s % m
        result ='{} дн {} час {} мин {} сек'.format(new_d, new_h, new_m, new_s);


    return result


duration = 400153
result = convert_time(duration)
print(result)
# в целом достаточно легко, но наличие болванки в ввиде функции сбивает с толку