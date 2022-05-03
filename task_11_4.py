'''4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов.
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
'''

class Storage:
    pass


class Office_equipment:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class Printer(Office_equipment):
    def __init__(self, brand, model, print_speed, printing_resolution):
        super().__init__(brand, model)
        self.print_speed = print_speed
        self.printing_resolution = printing_resolution

class Scaner(Office_equipment):
    def __init__(self, brand, model, color, scan_resolution):
        super().__init__(brand, model)
        self.color = color
        self.scan_resolution = scan_resolution

class Copier(Office_equipment):
    def __init__(self, brand, model, copy_speed):
        super().__init__(brand, model)
        self.copy_speed = copy_speed