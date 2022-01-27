def convert_list_in_str(list_in: list) -> str:
    """Обособляет каждое целое число кавычками, добавляя кавычку до и после элемента
        списка, являющегося числом, и дополняет нулём до двух целочисленных разрядов.
        Формирует из списка результирующую строковую переменную и возвращает."""
    # пишите реализацию своей программы здесь
    i = 0
    while i < len(my_list):
        if my_list[i].isdigit() and int(my_list[i]) < 10:
            my_list[i] = f'"0{my_list[i]}"'
            i += 1
        elif my_list[i].isdigit() and int(my_list[i]) >= 10:
            my_list[i] = f'"{my_list[i]}"'
            i += 1
        elif my_list[i] == '+5': # дайте пожалуйста наводку как найти в списке подобные элементы
            my_list[i] = f'"{my_list[i]}"'

        else:
            i += 1

    str_out = ' '.join(my_list)
    return str_out


my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = convert_list_in_str(my_list)
print(result)
