class My_err(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


if __name__ == "__main__":
    from sys import exit

    a = 0
    b = 0
    try:
        a = float(input("введите первое число: "))
        b = float(input("Введите второе число: "))
    except:
        print("incorrect input")
        exit(1)

    try:
        if b == 0:
            raise My_err("Ошибка деления на ноль")
        print(f"{a}/{b} = {a / b}")
    except My_err as err:
        print(err)

