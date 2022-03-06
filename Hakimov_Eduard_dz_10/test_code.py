



def Matrix(list):
    list_v = ''
    for i in range(len(list)):
        result = f'\t|{" ".join(map(str, first_matrix[i]))}|\n'
        list_v += result
    return list_v




first_matrix = [[1, 2], [3, 4], [5, 6]]
first_matrix_1 = [[1, 2], [3, 4], [5, 6]]
otvet = Matrix(first_matrix)
print(otvet)

matr = ''

matrix_result = [[num_1 + num_2 for num_1, num_2 in zip(row_1, row_2)]
              for row_1, row_2 in zip(first_matrix, first_matrix_1)
              ]



for i in range(len(first_matrix)):
    b = f'\t|{" ".join(map(str, first_matrix[i]))}|\n'
    #m = f'\t| {m} |\n'
    matr += b
print(matr)
print('\n')
print(matrix_result)

ls = [[5, 8], [9, 8]]
for i in range(len(ls)-1):
    if len(ls[i]) != len(ls[i+1]):
       raise ValueError('saa')

from abc import ABC, abstractmethod
class Test_one(ABC):
    @abstractmethod
    def sum(self):
        pass

class test_two(Test_one):
    def sum(self):
        print('h')
    def pt(self):
        print('z nen')

ter = test_two()
ter.sum()
print('\n')


"""
class Iterator:
    def __init__(self, start=0):
        self.i = start

    def __next__(self):
        self.i += 1
        if self.i <= 5:
            return self.i
        else:
            raise StopIteration

class IterObj:
    def __init__(self, start=0):
        self.start = start - 1

    def __iter__(self):
        return Iterator(self.start)


obj = IterObj(start=2)
for el in obj:
    print(el)
"""
"""
class Iter:
    def __init__(self, start=0):
        self.i = start - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i <= 5:
            return self.i
        else:
            raise StopIteration

obj = Iter(start=2)
for el in obj:
    print(el)
print('\n')

class MyClass:
    def __init__(self, param_1, param_2):
        self.param_1 = param_1
        self.param_2 = param_2

    @property
    def my_metod(self):
        return f'параметр класса'\
             f' {self.param_1}, {self.param_2}'
mc = MyClass('test1', 'test2')

print(mc.param_1)
print(mc.param_2)
print(mc.my_metod)
"""

class Auto:

    def __init__(self, year):
        self.year = year

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if year < 2000:
            self.__year = 2000
        elif year > 2019:
            self.__year = 2019
        else:
            self.__year = year

    def get_auto_year(self):
        return f'Атомобиль {str(self.year)}'

a = Auto(900)
print(a.get_auto_year())


d = 4
print(isinstance(d,int))



