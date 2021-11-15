class Stationery:
    title = ''

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    title = 'Ручка'

    def draw(self):
        print('Ручка пошла... Шк-шшшшшшк-шшшшк-шк')


class Pencil(Stationery):
    title = 'Карандаш'

    def draw(self):
        print('Карандаш в деле... Крк-хрккккк-хррррррк-хрк')


class Handle(Stationery):
    title = 'Маркер'

    def draw(self):
        print('А это маркер... Фук-фук-фук-фуууууук')


a = Stationery()
a.title = 'Канцелярия'
print(a.title)
print()

pen = Pen()
print(pen.title)
pen.draw()
print()

pencil = Pencil()
print(pencil.title)
pencil.draw()
print()

handle = Handle()
print(handle.title)
handle.draw()
