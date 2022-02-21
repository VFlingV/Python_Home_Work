
from datetime import datetime
class Woman:
# глобальный атрибут
    name: str = 'Emma'
    berthday: datetime = datetime(year=2004, month=2, day=20)

    def inr_y(self):
        print(f'i{self.__class__.name}')


    def get_info(self):
        print(f'ffff {self.name} sd {self.berthday.strftime("%d %B %Y")}')

    def say(self, mesage: str):
        print(f'{self.name} {mesage}')

girl = Woman()
print(girl)
girl.inr_y()
girl.get_info()
girl.say('s')
print('end')

class Warehouse:
    """Документирование класса в целом"""
    count: int = 0

    def new_build(self, storage_capasity: float, region: str):
        """Объявляет о постройке нового склада"""
        self.storage_capasity = storage_capasity
        self.region = region
        Warehouse.count += 1  # инкрементируем общее количество складов


warehouse_1 = Warehouse()
warehouse_1.new_build(555.55, 'Москва')
print(warehouse_1.storage_capasity, warehouse_1.region, f'Всего складов: {warehouse_1.count}')
warehouse_2 = Warehouse()
warehouse_2.new_build(150, 'Волгоград')
print(warehouse_2.storage_capasity, warehouse_2.region, f'Всего складов: {warehouse_2.count}')
print('\n')


import time


class People:
    """Так зарождалось всё человечество )))"""
    def __init__(self, name: str, birthday: datetime):
        self.name = name
        self.birthday = birthday

    def introduce_yourself(self):
        return f"I'm {self.__class__.__name__}", self.__get_info()

    def __get_info(self):
        return dict(name=self.name, birthday=self.birthday.strftime("%d %B %Y"))


class Man(People):
    sex: str = 'm'

    def working(self, sleeping: int = 5):
        """Мужик должен уметь работать"""
        while sleeping:
            print(f'Осталось спать секунд: {sleeping}')
            time.sleep(1)
            sleeping -= 1
        print('Поработали, теперь можно и домой!')


worker = Man('Данила', datetime(year=2001, month=11, day=17))
introduce_message, worker_info = worker.introduce_yourself()
print(f' {3 * "-//-"} '.join(map(str, [introduce_message, worker_info, type(introduce_message), type(worker_info)])))
# worker.working()
print('\n')

save_direction = ['направо', 'налево', 'прямо', 'назад']
print(save_direction.count('направо'))
save_direction_d = {'n': 'направо'}
