class Car:
    speed = 0
    color = ''
    name = ''
    is_police = bool

    def __init__(self, arg_2, arg_3, arg_4):
        self.color = arg_2
        self.name = arg_3
        self.is_police = arg_4

    def go(self, arg_1):
        self.speed = arg_1
        print('Машина поехала')

    def stop(self):
        self.speed = 0
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Скорость машины равно {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости в городе')
        else:
            print(f'Скорость машины равно {self.speed}')


class SportCar(Car):
    def go(self, arg):
        self.speed = arg
        print('Машина полетела')

    def stop(self):
        self.speed = 0
        print('Прилетели')

    def engine_sound(self):
        print('Ам-Амммммм-Амммммммммм...')  # Послушать рев двигателя


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Машина на пределе')
        else:
            print(f'Скорость машины равно {self.speed}')


class PoliceCar(Car):
    def turn_on_lights(self):  # Включить мигалки
        print('Мигалки включены')
        print('Би-бииип')


car_1 = Car('Красная', 'Хонда', True)
print(car_1.name, car_1.color)
car_1.go(50)
print(car_1.speed, 'км/ч')
car_1.turn('Направо')
car_1.stop()
print(car_1.speed, 'км/ч')
print()

car_2 = TownCar('Синяя', 'Мазда', False)
print(car_2.name, car_2.color)
car_2.go(70)
car_2.show_speed()
print()

car_3 = WorkCar('Черная', 'Волга', True)
print(car_3.name, car_3.color)
car_3.go(45)
car_3.show_speed()
print()

car_4 = SportCar('Зеленая', 'Ауди', True)
print(car_4.name, car_4.color)
car_4.go(330)
car_4.stop()
car_4.engine_sound()
print()

car_5 = PoliceCar('Белый', 'Джип', True)
print(car_5.name, car_5.color)
car_5.go(50)
car_5.turn_on_lights()
car_5.stop()
print()
