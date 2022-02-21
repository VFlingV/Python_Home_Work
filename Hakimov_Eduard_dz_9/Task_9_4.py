

class Car:
    is_police: bool = False


    def __init__(self, speed: int, color: str, name: str, police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = police
        """
        Конструктор класса
        :param speed: текущая скорость автомобиля
        :param color: цвет автомобиля
        :param name: название марки автомобиля
        """


    def go(self) -> None:
        """
        Увеличивает значение скорости на 15
        :return: в stdout сообщение по формату
            'Машина <название марки машины> повысила скорость на 15: <текущая скорость машины>'
        """
        self.speed += 15
        print(f'{self.name} повысила скорость на 15: {self.speed}')
        #return f'{self.name} повысила скорость на 15: {self.speed}'


    def stop(self) -> None:
        """
        При вызове метода скорость становится равной '0'
        :return: в stdout сообщение по формату '<название марки машины>: остановилась'
        """
        self.speed = 0
        print(f'{self.name}: остановилась')
        #return f'{self.name}: остановилась'


    def turn(self, direction: str) -> None:
        """
        Принимает направление движения автомобиля
        :param direction: строковое представление направления движения, может принимать только
            следующие значения: 'направо', 'налево', 'прямо', 'назад'
        :return: в stdout сообщение по формату
            '<название марки машины>: движется <direction>'
        """
        save_direction = ['направо', 'налево', 'прямо', 'назад']
        try:
            print(f'{self.name}: движется {direction}')
        except ValueError in ValueError:
            print(f'нераспознанное направление движения ')


    def show_speed(self):
        """
        Проверка текущей скорости автомобиля
        :return: в stdout выводит сообщение формата
            '<название марки машины>: текущая скорость <значение текущей скорости> км/час'
        """
        if not self.is_police:
            print(f'{self.name}: текущая скорость {self.speed} км/час')
            # return f'{self.name}: текущая скорость {self.speed} км/час'
        else:
            print(f'{self.name}: текущая скорость {self.speed}\nВруби мигалку и забудь про скорость!')


# определите классы TownCar, WorkCar, SportCar, PoliceCar согласно условия задания
class TownCar(Car): ...
class WorkCar(Car): ...
class PoliceCar(Car): ...
class SportCar(Car): ...
class Veler(ValueError):...


if __name__ == '__main__':
    town_car = TownCar(56, "red", 'WW_Golf')
    work_car = WorkCar(41, 'yellow', 'BobCat')
    police_car = PoliceCar(120, "blue", 'BMW', True)
    sport_car = SportCar(300, 'white', 'Ferrari')
    town_car.go()  # Машина WW_Golf повысила скорость на 15: 56
    town_car.show_speed() # WW_Golf: текущая скорость 56 км/час
    work_car.show_speed()  # Alarm!!! Speed!!!
    town_car.stop()  # WW_Golf: остановилась
    police_car.show_speed()
    # BMW: текущая скорость 120 км/час
    # Вруби мигалку и забудь про скорость!
    sport_car.turn('назад')  # Ferrari(SportCar): движется назад
    sport_car.turn('right')
    sport_car.go()
    """
    Traceback (most recent call last):
      ...
    ValueError: нераспознанное направление движения
    """
save_direction = ['направо', 'налево', 'прямо', 'назад']
save_direction_d = {'n': 'направо'}
print(save_direction_d.get('п'))
