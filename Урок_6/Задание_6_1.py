import time


class TrafficLight:
    _color = ''

    def running(self):
        while True:
            __color = 'Красный'
            print('Цвет светофора : ', __color)
            time.sleep(7)
            _color = 'Желтый'
            print('Цвет светофора : ', __color)
            time.sleep(2)
            _color = 'Зеленый'
            print('Цвет светофора : ', __color)
            time.sleep(4)


a = TrafficLight()
a.running()
