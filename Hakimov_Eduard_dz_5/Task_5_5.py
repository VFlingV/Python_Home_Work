

def get_uniq_numbers(src: list):
    save_num = set()
    tmp_num = set()
#    result = []
    for el in src:
        if el not in tmp_num:
            save_num.add(el)
        else:
            save_num.discard(el)
        tmp_num.add(el)
    result =[n for n in src if n in save_num]
    return result


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(*get_uniq_numbers(src))

#for n in src:
#    if n in save_num:
#        result.append(n)

