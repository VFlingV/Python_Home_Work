# Задание 3
def transform_string(number: int) -> str:
    if (number - 1) % 10 == 0 and number != 11:
        return f'{number} процент'
    elif (number - 2) % 10 == 0 and number != 12:
        return f'{number} процента'
    elif (number - 3) % 10 == 0 and number != 13:
        return f'{number} процента'
    elif (number - 4) % 10 == 0 and number != 14:
        return f'{number} процента'
    else:
        return f'{number} процентов'



for n in range(1, 101):
    print(transform_string(n))
    # самая легкая задача. надеюсь все правильно....