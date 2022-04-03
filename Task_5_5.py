# 5. Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
# Представлен список чисел.
# Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования
# в исходном списке, например:

from sys import getsizeof
from time import perf_counter


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]

# Решение 1
start = perf_counter()
unique = []
for i in range(len(src)):
    for num in range(len(src)):
        if i != num and src[i] == src[num]:
            break
    else:
        unique.append(src[i])
print('Решение №1:', unique)
print('Время: ', perf_counter() - start)
print('Размер: ', getsizeof(unique), '\n')

# Решение 2. Как сохранить размер, не смогла понять, но время уменьшилось
# Может, если только как в прошлом задании сделать генератор и
# вывести уже не список.
# Или же сделать генератор, а потом в список добавить все.

start = perf_counter()
unique = [el for el in src if src.count(el) == 1]
print('Решение №2:', unique)
print('Время: ', perf_counter() - start)
print('Размер: ', getsizeof(unique))