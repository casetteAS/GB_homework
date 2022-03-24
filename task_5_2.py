def odd_nums(n):
    c = (i for i in range(n) if i % 2 != 0)
    return c

odd_to_15 = odd_nums(15)

print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))