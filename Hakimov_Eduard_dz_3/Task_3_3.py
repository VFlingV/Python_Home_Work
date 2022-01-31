def thesaurus(*args) -> dict:
    # пишите свою реализацию здесь
    dict_out = {
    }
    for name in [*args]:
        if name[0] in dict_out.keys():
            dict_out[name[0]].append(name)
        else:
            dict_out[name[0]] = [name]
    #dict_out = name_save  # результирующий словарь значений
    return dict_out


print(thesaurus("Иван", "Иван", "Мария", "Петр", "Илья"))
