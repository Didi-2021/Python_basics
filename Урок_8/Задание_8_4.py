class OfficeEquipmentWarehouse:
    wh_name = ''
    wh_address = ''


class OfficeEquipment(OfficeEquipmentWarehouse):
    eq_name = ''
    insurance = bool  # Наличие страховки


class Printer(OfficeEquipment):
    eq_name = 'Принтер'
    feature = 3  # 3 в 1, 2 в 1 или 1

    def __init__(self, wh_name, wh_address, insurance, feature):
        self.wh_name = wh_name
        self.wh_address = wh_address
        self.insurance = insurance
        self.feature = feature

    def show(self):
        print(self.wh_name, self.wh_address, self.eq_name, self.feature, self.insurance)


class Scanner(OfficeEquipment):
    eq_name = 'Сканер'
    feature = 'Цв'  # Ч/б

    def __init__(self, wh_name, wh_address, insurance, feature):
        self.wh_name = wh_name
        self.wh_address = wh_address
        self.insurance = insurance
        self.feature = feature

    def show(self):
        print(self.wh_name, self.wh_address, self.eq_name, self.feature, self.insurance)


class Copier(OfficeEquipment):
    eq_name = 'Ксерокс'
    feature = 5  # Копий в минуту

    def __init__(self, wh_name, wh_address, insurance, feature):
        self.wh_name = wh_name
        self.wh_address = wh_address
        self.insurance = insurance
        self.feature = feature

    def show(self):
        print(self.wh_name, self.wh_address, self.eq_name, self.feature, self.insurance)


printer = Printer('Первый скдад', 'Питер', True, 2)
scanner = Scanner('Второй скдад', 'Воронеж', True, 'Ч/б')
copier = Copier('Трейтий скдад', 'Новосибирск', False, 10)
printer.show()
scanner.show()
copier.show()
