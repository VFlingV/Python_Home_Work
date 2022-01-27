from random import uniform
def transfer_list_in_str(list_in: list) -> str:
    """Преобразует каждый элемент списка (вещественное число) в строку вида '<r> руб <kk> коп' и
        формирует из них единую строковую переменную разделяя значения запятой."""
    # пишите реализацию своей программы здесь
    result = []
    for i in list_in:
        rub = int(i) # заганяем значение в int тем самым отделяем число до точки
        c = (i * 100) % 100 # такой вариант  подсказал хабр... каюсь нагло спер идею
        result.append(f'{rub} руб {int(c):02} коп')
    result = ", ".join(result) # обеденяем строку в список

    str_out = result
    return str_out


my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]  # автоматическая генерация случайных 15 чисел
print(f'Исходный список: {my_list}')
result_1 = transfer_list_in_str(my_list)
print(f'a = ', result_1)


def sort_prices(list_in: list) -> list:
    """Сортирует вещественные числа по возрастанию, не создавая нового списка"""
    # пишите реализацию здесь
    # sorted
    list_in.sort()
    return list_in


# зафиксируйте здесь информацию по исходному списку my_list
result_2 = sort_prices(my_list)
# зафиксируйте здесь доказательство, что результат result_2 остался тем же объектом
if id(my_list) == id(result_2):
    print('id объекта не изменился ')
print(f'b = ', result_2)


def sort_price_adv(list_in: list) -> list:
    """Создаёт новый список и возвращает список с элементами по убыванию"""
    # пишите реализацию здесь

    list_out = sorted(list_in, reverse=True)
    return list_out


result_3 = sort_price_adv(my_list)
print(f'c = ', result_3)


def check_five_max_elements(list_in: list) -> list:
    """Проверяет элементы входного списка вещественных чисел и возвращает
        список из ПЯТИ максимальных значений"""
    # пишите реализацию здесь
    list_in = sorted(list_in)
    list_out = list_in[10:]
    list_out.reverse()
    return list_out


result_4 = check_five_max_elements(my_list)
print(f'd = ', result_4)
