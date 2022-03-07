class Office_equipment:

    def __init__(self, name, quantity, number_of_lists, *args):
        self.name = name
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель устройства': self.name, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name}  количество {self.quantity}'

    def reception(self):
        try:
            unit = input(f'Введите наименование ')
            unit_q = int(input(f'Введите количество '))
            unique = {'Модель устройства': unit, 'Количество': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Текущий список -\n {self.my_store}')
        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода - Q, продолжение - Enter')
        q = input(' ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад -\n {self.my_store_full}')
            return f'Выход'
        else:
            return Office_equipment.reception(self)


class Printer(Office_equipment):
    def to_print(self):
        return f'to print smth {self.numb} times'


class Scanner(Office_equipment):
    def to_scan(self):
        return f'to scan smth {self.numb} times'


class Copier(Office_equipment):
    def to_copier(self):
        return f'to copier smth  {self.numb} times'


unit_1 = Printer('hp', 2000, 5, 10)
unit_2 = Scanner('Canon', 1200, 5, 10)
unit_3 = Copier('KYOCERA', 150, 6, 15)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_3.to_copier())
