### 4. Представлен список чисел.
# Необходимо вывести те его элементы, значения которых больше предыдущего, например:
from sys import getsizeof
from time import perf_counter

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]

# Решение №1
start = perf_counter()
result = []
for i in range(1, len(src)):
    if src[i] > src[i-1]:
        result.append(src[i])
print('Решение №1: ', result)
print('Память: ', getsizeof(result))
print('Время: ', perf_counter() - start, '\n')

# Решение №2
start = perf_counter()
result = (src[i] for i in range(1, len(src)) if src[i] > src[i-1])
print('Решение №2: ', *result)
print('Память: ', getsizeof(result))
print('Время: ', perf_counter() - start)