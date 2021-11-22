class Date:
    def __init__(self, str_date):  # вводится дата в виде строки ДД-ММ-ГГГГ
        self.date = str_date
        '''self.day = str_date[0:2]
        self.month = str_date[3:5]
        self.year = str_date[-4:]'''

    @classmethod
    def conversion_to_numbers(cls, str_date):
        return [int(str_date[0:2]), int(str_date[3:5]), int(str_date[-4:])]

    @staticmethod
    def validation(str_date):
        date_list = Date.conversion_to_numbers(str_date)
        '''day = int(str_date[0:2])
        month = int(str_date[3:5])
        year = int(str_date[-4:])'''
        day = date_list[0]
        month = date_list[1]
        year = date_list[2]

        # Февраль
        if month == 2:
            if (day <= 0) or (day >= 30) or (year < 0):
                print('Некорректная дата')
            else:
                print('Корректная дата')

        # 30 дней в месяце
        elif (month == 4) or (month == 6) or (month == 9) or (month == 11):
            if (day <= 0) or (day >= 31) or (year < 0):
                print('Некорректная дата')
            else:
                print('Корректная дата')

        # 31 день в месяце
        elif (month == 1) or (month == 3) or (month == 5) or (month == 7) or (month == 8) \
                or (month == 10) or (month == 12):
            if (day <= 0) or (day > 31) or (year < 0):
                print('Некорректная дата')
            else:
                print('Корректная дата')

        else:
            print('Некорректная дата')


print(Date.conversion_to_numbers('01-01-2001'))
print(type(Date.conversion_to_numbers('01-01-2001')))

print(Date.conversion_to_numbers('01-01-2001')[2])
print(type(Date.conversion_to_numbers('01-01-2001')[2]))

d_1 = Date('01-02-2001')
print(d_1.date)
print(type(d_1))
print(type(d_1.date))

Date.validation('10-30-2000')
Date.validation('10-10-2000')
Date.validation('-1-30-2000')
Date.validation('10-10-0001')
Date.validation('10-30-0000')
Date.validation(d_1.date)
Date.validation('10-02-9999')
Date.validation('30-02-9999')
