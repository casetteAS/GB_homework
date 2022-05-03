'''5. Разработайте методы, которые отвечают за приём оргтехники на склад
и передачу в определённое подразделение компании. Для хранения данных о
наименовании и количестве единиц оргтехники, а также других данных, можно
использовать любую подходящую структуру (например, словарь).'''

class Storage:
    def __init__(self):
        self._accepted = []

    def __str__(self):
        return f'{self._accepted}'

    def reception(self, *equipments):
        for equipment in equipments:
            self._accepted.append(equipment)
        return self._accepted

    def transfer(self, department, *equipments):
        for equipment in equipments:
            if not equipment in self._accepted:
                raise Exception('Запрашиваемого товара нет на складе')
            department.list_of_department.append(equipment)
            self._accepted.remove(equipment)
            return self._accepted


class Departments:

    def __init__(self):
        self._equipment = []

    def __str__(self):
        return f'{self._equipment}'

    @property
    def list_of_department(self):
        return self._equipment


class Department1(Departments):
    pass


class Department2(Departments):
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


class Scanner(Office_equipment):
    def __init__(self, brand, model, color, scan_resolution):
        super().__init__(brand, model)
        self.color = color
        self.scan_resolution = scan_resolution


class Copier(Office_equipment):
    def __init__(self, brand, model, copy_speed):
        super().__init__(brand, model)
        self.copy_speed = copy_speed

printer = Printer('HP', 'HP Deskjet IA Ultra 4828', '7,5/5,5 стр/мин', 1200)
scanner = Scanner('Espada', 'Espada E-IScan 2.0', 'цветной', 1050)
copier = Copier("Canon", 'PIXMA G2411', 5)
storage = Storage()
storage.reception(printer, scanner, copier)
print(storage)
department1 = Department1()
storage.transfer(department1, printer)
print(department1)
department2 = Department2()
storage.transfer(department2, scanner, copier)
print(storage)
print(department2)