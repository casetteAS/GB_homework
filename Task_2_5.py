# Задание 5

# A
# [57.8, 46.51, 97, ...]
# Вывести на экран эти цены через запятую в одну строку,
# цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»).
# Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек
# (должно быть 07 коп или 00 коп).

prices = [57.8, 46.51, 97, 23.1, 45, 45.09, 94.45, 57, 80.57, 100]
print('A) Цены:')
print(id(prices))

for i in range(len(prices)):
    price = str(float(prices[i]))
    price = price.split('.')
    price = f'{int(price[0]):.0f} руб {int(price[1]):0>2d} коп'
    print(price,end=' ')
    if i != len(prices) - 1:
        print(end=', ')
print(end = '\n')
print(end = '\n')

# B
# Вывести цены, отсортированные по возрастанию, новый список не создавать
# (доказать, что объект списка после сортировки остался тот же).

prices.sort()
print('B) Цены, отсортированные по возрастанию: ')
print(id(prices))
for i in range(len(prices)):
    price = str(float(prices[i]))
    price = price.split('.')
    price = f'{int(price[0]):.0f} руб {int(price[1]):0>2d} коп'
    print(price,end=' ')
    if i != len(prices) - 1:
        print(end=', ')
print(end = '\n')
print(end = '\n')

# C
# Создать новый список, содержащий те же цены, но отсортированные по убыванию.

prices = sorted(prices, reverse=True)
print('C) Цены, но отсортированные по убыванию: ')
print(id(prices))
for i in range(len(prices)):
    price = str(float(prices[i]))
    price = price.split('.')
    price = f'{int(price[0]):.0f} руб {int(price[1]):0>2d} коп'
    print(price,end=' ')
    if i != len(prices) - 1:
        print(end=', ')
print(end = '\n')
print(end = '\n')
# D
# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

print('D) Самые дорогие 5 товаров: ')
prices = prices[:5]

for i in range(len(prices)):
    price = str(float(prices[i]))
    price = price.split('.')
    price = f'{int(price[0]):.0f} руб {int(price[1]):0>2d} коп'
    print(price,end=' ')
    if i != len(prices) - 1:
        print(end=', ')
print(end = '\n')