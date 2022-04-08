'''3. Написать декоратор для логирования типов позиционных аргументов функции, например:
def type_logger...
...
@type_logger
def calc_cube(x):
return x ** 3
a = calc_cube(5)
5: <class 'int'>
Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете
ли вы вывести тип значения функции? Сможете ли решить задачу для именованных
аргументов? Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя
функции, например, в виде:
a = calc_cube(5)
calc_cube(5: <class 'int'>)
'''

from functools import wraps
# декоратор
def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        for a in args:
            print(a, ':', type(a))
        for k in kwargs:
            print(k, ':', type(k))
    return wrapper


@type_logger
# функция
def calc_cube(*args):
    generator_cub = [x ** 3 for x in args]
    return generator_cub

a = calc_cube(5, 6, 7, 3)

# для именованных аргументов
def type_logger_name(func):
    @wraps(func)
    def wrapper(x):
        func(x)
        print(x, ':', type(x))
    return wrapper

@type_logger_name
# функция
def calc_cube(x):
    return x ** 2

b = calc_cube(5)

# Сможете ли вывести имя # функции, например, в виде:
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)

def type_logger_name(func):
    @wraps(func)
    def wrapper(x):
        func(x)
        print(func. __name__,'(', x, ':', type(x), ')')
    return wrapper

@type_logger_name
# функция
def calc_cube(x):
    return x ** 2

c = calc_cube(5)
