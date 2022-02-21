class Stationery:


    def __init__(self, title: str) -> None:
        self.title_save = str(title)


    def draw(self) -> None:
        # не дошло как реализовать вывод "Запуск отрисовки" кроме как через условие
        if self.__class__.__name__ == 'Pencil':
            print(f'Запуск отрисовки\n{self.__class__.__name__}:приступил к отрисовке объекта "{self.title_save}"')
            #return f'Запуск отрисовки\n{self.__class__.__name__}:приступил к отрисовке объекта "{self.title_save}"'
        else:
            print(f'{self.__class__.__name__}:приступил к отрисовке объекта "{self.title_save}"')
            #return f'{self.__class__.__name__}:приступил к отрисовке объекта "{self.title_save}"'


# определите классы ниже согласно условий задания
class Pen(Stationery):...
class Pencil(Stationery):
    def start(self):
        print('Запуск отрисовки')
class Handle(Stationery): ...


if __name__ == '__main__':
    pen = Pen('Ручка')
    pencil = Pencil('Карандаш')
    handle = Handle('Маркер')
    pen.draw()  # Pen: приступил к отрисовке объекта "Ручка"
    handle.draw()  # Handle: приступил к отрисовке объекта "Маркер"
    #pencil.start()
    pencil.draw()  # Пример вывода ниже в многострочном комментарии
    """
    Запуск отрисовки
    Pencil: приступил к отрисовке объекта "Карандаш"
    """





