class Worker:
    name = ''
    surname = ''
    position = ''
    _income = {'wage': 0, 'bonus': 0}


class Position(Worker):
    def get_full_name(self):
        print(f'Имя : {self.name} \nФамилия : {self.surname}')

    def get_total_income(self):
        income = self._income["wage"] + self._income["bonus"]
        print(f'Общий доход : {income}')


pers_1 = Worker()
pers_1.name = 'Иван'
pers_1.surname = 'Иванов'
pers_1.position = 'Техник'
pers_1._income['wage'] = 1000
pers_1._income['bonus'] = 500

print(pers_1.name, pers_1.surname, pers_1.position, pers_1._income, '\n')

look_pers_2 = Position()
look_pers_2.name = 'Петр'
look_pers_2.surname = 'Петров'
look_pers_2.position = 'Инженер'
look_pers_2._income['wage'] = 700
look_pers_2._income['bonus'] = 100
look_pers_2.get_full_name()
look_pers_2.get_total_income()
