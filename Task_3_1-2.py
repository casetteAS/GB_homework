# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None.
# Подумайте, как и где лучше хранить информацию, необходимую для перевода:
# какой тип данных выбрать, в теле функции или снаружи.
numbers = {'zero': '"ноль"', 'one': '"один"', 'two': '"два"','three': '"три"',
           'four': '"четыре"', 'five': '"пять"', 'six': '"шесть"', 'seven': '"семь"', 'eight': '"восемь"', 'nine': '"девять"', 'ten': '"десять"'}


def num_translate(number):
    for en, rus in numbers.items():
        if en == number:
            print(rus)
        elif en.title() == number:
            print(rus.title())


num_translate('asd')
num_translate('zero')
num_translate('three')
num_translate('Nine')