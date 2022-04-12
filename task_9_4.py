'''4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.'''
from random import choice

class Car:
    is_police = False
    def __init__(self, speed, color, name):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = False

    def show_info(self):
        return f'Скорость: {self.speed} км/ч, цвет: {self.color}, марка: {self.name}, полиция: {self.is_police}'

    def go(self):
        return f'Машина поехала'

    def stop(self):
        return f"Машина остановилась"

    def direction(self):
        return f'{choice(["Машина повернула направо", "Машина повернула налево"])}'

    def show_speed(self): #текущая скорость автомобиля
        return f'Текущая скорость машины: {self.speed}'

class TownCar(Car): #переопределить метод show_speed При значении скорости свыше 60 должно выводиться сообщение о превышении скорости.

    def show_speed(self):
        if self.speed > 60:
            return f'Скорость машины слишком высока. Вам следует придерживаться скорости меньше 60'
        return f'{self.speed} км/ч'


class SportCar(Car):
    pass


class WorkCar(Car): #переопределить метод шоу спид При значении скорости свыше 40 должно выводиться сообщение о превышении скорости.

    def show_speed(self):
        if self.speed > 40:
            return f'Скорость машины слишком высока. Вам следует придерживаться скорости меньше 60'
        return f'{self.speed} км/ч'

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True


# a = Car(60, "Зеленый", "Мазда")
# print(a.go())
# print(a.direction())
# print(a.stop())
# print(a.show_speed())
# t = TownCar(70, 'Синий', 'Тойота Камри')
# print(t.show_speed())
# w = WorkCar(38, 'Красный', 'Киа Риа')
# print(w.show_speed())
# s = SportCar(80, 'Желтый', 'Спорт')
# print(s.show_info())
p = PoliceCar(70, 'Белый', 'Полиция')
print(p.show_info())
