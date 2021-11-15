class Road:
    _length = 0
    _width = 0

    def __init__(self, arg_1, arg_2):
        Road._length = arg_1
        Road._width = arg_2

    def road_mass(self, arg):
        mass = Road._width * Road._length * 25 * arg
        print(mass, 'кг')


a = Road(20, 5000)
depth = 5
a.road_mass(depth)
