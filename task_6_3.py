# 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь,
# разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов
# и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.
# Сохранить словарь в файл. Проверить сохранённые данные.
# Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО,
# задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1».
# При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
from itertools import zip_longest
import pickle

users = []
hobbies = []

with open('users.csv.txt', encoding='utf-8') as f:
    for i in f.readlines():
        user = i.replace(',', ' ').replace('\n', '') #Убираем ненужные символы
        users.append(user)
with open('hobby.csv.txt', encoding='utf-8') as f:
    for i in f.readlines():
        hobby = i.replace('\n', '') #Убираем ненужные символы
        hobbies.append(hobby)

if len(users) > len(hobby): #Если записей в хобби больше, чем в юзерах, то выход с 1
    exit(1)

my_dict = {user: hobby for (user, hobby) in zip_longest(users, hobbies)}
with open('my_dict.pickle', 'wb') as f:
    pickle.dump(my_dict, f)
with open('my_dict.pickle', 'rb') as f:
    print(pickle.load(f))