class Warehouse:
    wh_count = 0  # Количество складов
    number = 0  # Номер склада
    all_wh_count = 0  # Число всей техники на складе
    pnt_wh_count = 0  # Число принтеров на складе
    scan_wh_count = 0  # Число сканеров на складе
    prod_list = []  # Список куда, сколько техники отправлено

    def __init__(self):
        Warehouse.wh_count += 1
        self.number += Warehouse.wh_count

    @classmethod
    def show(cls):
        print(f'Всего складов : {cls.wh_count}')

    def show_wh(self):
        print(f'На складе №{self.number}. '
              f'Всего техники : {self.all_wh_count}; '
              f'Всего принтеров : {self.pnt_wh_count}; '
              f'Всего сканеров : {self.scan_wh_count}.')

    def reception(self, equip):
        if equip.eq_name == 'Принтер':
            self.pnt_wh_count += equip.pnt_count
            self.all_wh_count += equip.pnt_count
        elif equip.eq_name == 'Сканер':
            self.scan_wh_count += equip.scan_count
            self.all_wh_count += equip.scan_count


class OfficeEquipment:
    all_eq_count = 0  # Число всей техники
    all_pnt_count = 0  # Число всех принтеров
    all_scan_count = 0  # Число всех сканеров
    # all_eq_list = []  # Список куда сколько техники отправлено

    @classmethod
    def show(cls):
        return print(f'Всего техники : {OfficeEquipment.all_eq_count} '
                     f'Всего принтеров : {OfficeEquipment.all_pnt_count} '
                     f'Всего сканеров : {OfficeEquipment.all_scan_count}')


class Printer(OfficeEquipment):
    eq_name = 'Принтер'
    pnt_count = 0

    def __init__(self, count):
        OfficeEquipment.all_eq_count += count
        OfficeEquipment.all_pnt_count += count
        self.pnt_count = count


class Scanner(OfficeEquipment):
    eq_name = 'Сканер'
    scan_count = 0

    def __init__(self, count):
        OfficeEquipment.all_eq_count += count
        OfficeEquipment.all_scan_count += count
        self.scan_count = count


p1 = Printer(2)
s1 = Scanner(3)
p2 = Printer(10)
s2 = Scanner(20)

OfficeEquipment.show()

wh1 = Warehouse()
wh2 = Warehouse()
wh3 = Warehouse()
Warehouse.show()

wh1.reception(p1)
wh1.show_wh()

wh2.reception(s1)
wh2.show_wh()

wh3.show_wh()
wh3.reception(p2)
wh3.show_wh()
wh3.reception(s2)
wh3.show_wh()
