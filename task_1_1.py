# ### 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности
# duration в секундах: до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
# Примеры:
# duration = 53
# 53 сек
# duration = 153
# 2 мин 33 сек
# duration = 4153
# 1 час 9 мин 13 сек
# duration = 400153
# 4 дн 15 час 9 мин 13 сек
duration = int(input('Введите число: '))
if 0 <= duration < 60:
    time = f'{duration} сек'
    print(time)
elif 60 <= duration < 3600:
    s = duration % 60
    m = duration // 60
    time = f'{m} мин, {s} сек'
    print(time)
elif 3600 <= duration < 86400:
    s = duration % 60
    m = duration % 3600 // 60
    h = duration // 3600
    time = (f'{h} час, {m} мин, {s} сек')
    print(time)
elif 86400 <= duration < 604800:
    s = duration % 60
    m = duration % 3600 // 60
    h = duration % 86400 // 3600
    d = duration // 86400
    time = f'{d} дн., {h} час., {m} мин., {s} сек.'
    print(time)
else:
    print(' Введеное число выходит за пределы расчетов\n','Число будет отображать секунды, а мы покажем Вам время в днях, часах, минутах, секундах')


