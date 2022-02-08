def convert_name_extract(list_in: list) -> list:
    """Извлекает имена из элементов и формирует список приветствий."""
    # пишите реализацию своей программы здесь
    name_save = []
    for i in range(len(list_in)):
        share_list = list_in[i].split(' ')# разбивает строку по указанному разделителю
        list_ind = len(share_list) - 1 # забираем последний элемент списка
        name = share_list[list_ind]
        new_name = name.capitalize() # приводим текст к нужному формату имени
        new_name = f'Привет, {new_name}!'
        name_save.append(new_name)
    list_in.clear()
    list_in.extend(name_save)
    list_out = name_save
    return list_out


my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
result = convert_name_extract(my_list)
print(result)
