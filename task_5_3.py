# 3. Есть два списка:
# Необходимо реализовать генератор, возвращающий кортежи вида
# (<tutor>, <klass>), например:
# ('Иван', '9А')
# ('Анастасия', '7В')
# ...
# Количество генерируемых кортежей не должно быть больше длины
# списка tutors. Если в списке klasses меньше элементов,
# чем в списке tutors, необходимо вывести последние кортежи в виде:
# (<tutor>, None), например:
# ('Станислав', None)
# ### Доказать, что вы создали именно генератор.
# Проверить его работу вплоть до истощения.
# Подумать, в каких ситуациях генератор даст эффект.

# None не стала создавать, так как количество учителей меньше,
# чем классов

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
gen_of_klasses = ((tutors[i], klasses[i]) for i in range(len(tutors)))
print(type(gen_of_klasses))
print(next(gen_of_klasses))
print(next(gen_of_klasses))
print(next(gen_of_klasses))
print(next(gen_of_klasses))
print(next(gen_of_klasses))
print(next(gen_of_klasses))
print(next(gen_of_klasses))

# генератор нужен, когда объемы данных слишком большие, и нам не нужно хранить всю информацию.
# К примеру, мы делаем запрос по поиску какого-либо файла на компьютере, и поиск
# нам сразу начинает выдавать определенный файл с таким названием. Иначе бы только после полного поиска
# (который бы занял много времени) нам бы выдали необходимые документы.
