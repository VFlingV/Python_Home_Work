"""""
Выяснить тип результата выражений:
15 * 3
15 / 3
15 // 2
15 ** 2
"""""

save_num_1 = []
i = 15 * 3
b = 15 / 3
c = 15 // 2
d = 15 ** 2
save_num_1.extend([i, b, c, d]) # изначально использовал  .append, но дошло что .extend лучше подходит
print(save_num_1)

n = 0

while n < len(save_num_1):
    print(save_num_1[n], '=', type(save_num_1[n]))
    n += 1

