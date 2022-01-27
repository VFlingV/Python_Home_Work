# задание 2
# сломал весь мозг, но нормально сделать не успел


cubed_numbers =[]
suma_cubed_num = 0
for numbers in list(range(1, 1000, 2)):
    cubed_numbers.append(numbers **3)


for ind, cubed_cell in enumerate(cubed_numbers):
    sum_numbers = 0
    while cubed_cell > 0:
        sum_numbers += cubed_cell % 10
        cubed_cell //=10
    if sum_numbers % 7 == 0:
        suma_cubed_num += cubed_numbers[ind]
print(suma_cubed_num)

for ind in range(len(cubed_numbers)):
    cubed_numbers[ind] +=17
suma_cubed_num = 0

for ind, cubed_cell in enumerate(cubed_numbers):
    sum_numbers = 0
    while cubed_cell > 0:
        sum_numbers += cubed_cell % 10
        cubed_cell //= 10
    if sum_numbers % 7 == 0:
        suma_cubed_num += cubed_numbers[ind]
print(suma_cubed_num)
