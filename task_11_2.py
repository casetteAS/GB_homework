'''2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна корректно
обработать эту ситуацию и не завершиться с ошибкой.
'''

class DIVISION_BY_ZERO:

    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def division(self):
        try:
            result = self.num_1 / self.num_2
            return f'Результат деления = {result}'
        except ZeroDivisionError:
            return 'На ноль делить нельзя'

a = DIVISION_BY_ZERO(6, 3)
print(a.division())
a = DIVISION_BY_ZERO(6, 0)
print(a.division())