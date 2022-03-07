from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, value):
        self.value = float(value)


    @property    # изначально думал будет достаточно тут прописать @property
    @abstractmethod
    def calculate(self):
        pass


class Coat(Clothes):
    @property
    def calculate(self):
        result = round(self.value / 6.5 + 0.5, 2)
        return result


class Costume(Clothes):
    @property
    def calculate(self):
        result = round(2 * self.value + 0.3, 2)
        return result


if __name__ == '__main__':
    coat = Coat(45.0)
    costume = Costume(3)

    print(coat.calculate)  # 7.42
    print(costume.calculate)  # 6.3
    #print(type(costume.calculate))
"""
есть ли смысл решать эту задачу используя .setter? изучал этот момент, но как испульзовать и не усложнив задачу,
так и не придумал 
"""
