# 1. Написать генератор нечётных чисел от 1 до n (включительно),
# используя ключевое слово yield, например:

def odd_nums(n):
    for i in range(n):
        if i % 2 != 0:
            yield i

odd_to_15 = odd_nums(15)
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
