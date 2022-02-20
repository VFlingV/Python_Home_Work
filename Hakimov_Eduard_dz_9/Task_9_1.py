
import time


class TrafficLight:
    __color: str = ' '


    def running(self):


        def start(color: str, time_on: int):
            self.__color = color
            print(f'{self.__color} {time_on} сек')
            while time_on:
                time.sleep(time_on)
                time_on -= 1


        red = start('red', 4)
        yellow = start('yellow', 2)
        green = start('green', 3)



if __name__ == '__main__':
    traffic = TrafficLight()
    traffic.running()


