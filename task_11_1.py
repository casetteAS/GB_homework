
'''1. Реализовать класс «Дата», функция-конструктор которого должна прнимать дату
в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать
их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры
# на реальных данных.'''


# Я знаю что data - данные, а не дата. Его удобнее использовать

class Data:
    def __init__(self, data):
        self.data = data

    @classmethod
    def num_data(cls, data):
        date, month, year = data.split('-')
        return f'Число {date}, месяц {month}, год {year}'

    @staticmethod
    def validation(data):
        date, month, year = data.split('-')
        if int(date) >= 31:
            raise ValueError('Формат даты неверен. Дата должна быть от 1 до 31')
        if int(month) > 12:
            raise ValueError('Формат месяца неверен. Формат месяца от 1 до  12')
        if int(year) <= 0:
            raise ValueError('Формат года неверен')
        return data



print(Data.num_data('12-12-2020'))
Data.validation('13-07-2022')