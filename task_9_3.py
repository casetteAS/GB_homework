'''3. Реализовать базовый класс Worker (работник).
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные,
 проверить значения атрибутов, вызвать методы экземпляров.'''
from decimal import Decimal
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        return f'Полное имя: {self.name} {self.surname}'
    def get_total_income(self):
        result = Decimal(self._income["wage"]) + Decimal(self._income["bonus"])
        return f'Доход: {result}'

p = Position('Kate', 'Rock', 'manager', 50000, 25000)
print(p.get_full_name())
print(p.get_total_income())
print(p.name)
print(p.surname)
print(p.position)

