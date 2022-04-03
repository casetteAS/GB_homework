'''2. *(вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей
структурой:
|--my_project
|--settings
| |--__init__.py
| |--dev.py
| |--prod.py
|--mainapp
| |--__init__.py
| |--models.py
| |--views.py
| |--templates
|   |--mainapp
|       |--base.html
|       |--index.html
|--authapp
| |--__init__.py
| |--models.py
| |--views.py
| |--templates
|   |--authapp
|       |--base.html
|       |--index.html
Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом
текстовом редакторе «руками» (не программно); предусмотреть возможные исключительные
ситуации, библиотеки использовать нельзя'''
import os
import yaml

folders = {
    'my_project':
        [{'settings':
              ['__init__.py', 'dev.py', 'prod.py']},
         {'mainapp':
              ['__init__.py', 'models.py', 'views.py', {'templates':
                                                             [{'mainapp':
                                                                   ['base.html', 'index.html']}]}]},
         {'authapp':
             ['__init__.py', 'models.py', 'views.py', {'templates':
                                                            [{'authapp':
                                                                  ['base.html', 'index.html']}]}]}]}

with open('config.yaml', 'w') as f:
    f.write(yaml.dump(folders))
with open('config.yaml') as f:
    folders_yaml = yaml.load(f, Loader=yaml.FullLoader)
    # print(folders_yaml)

def create_folder(path): #сразу создадим проверку существования папки
    if not os.path.exists(path):
        os.mkdir(path)

def build_starter(data):
    for folder, data_tmp in data.items():
        create_folder(folder)
        os.chdir(folder) # входим в созданную директорию
        for d in data_tmp:
            if isinstance(d, dict): #является ли объект словарем, если да, реализуем рекурсию
                build_starter(d)
            else: # Если это не словарь и
                if not os.path.exists(d): #если такого файла еще нет и
                    if '.' in d: #если в тексте есть точка, то создаем файл
                        with open(d, 'w') as f:
                            f.write('')
    else:
        os.chdir('../')

build_starter(folders_yaml)