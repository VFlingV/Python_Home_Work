class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        print(f'Сумма равна')
        return f'{self.a + other.a}, {self.b + other.b}'

    def __mul__(self, other):
        print(f'Произведение равно')
        return f'{self.a * other.a - (self.b * other.b)}, {self.b * other.a}'

    def __str__(self):
        return f'{self.a}, {self.b}'


num_1 = Complex(1, 2)
num_2 = Complex(3, 4)
print(num_1 + num_2)
print(num_1 * num_2)