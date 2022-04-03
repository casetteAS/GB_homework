'''1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей
структурой папок:
|--my_project
|--settings
|--mainapp
|--adminapp
|--authapp
Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); как
лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена
папок под конкретный проект; можно ли будет при этом расширять конфигурацию и хранить
данные о вложенных папках и файлах (добавлять детали)?
'''
import os

# Решила сделать модулем

def create_folder(path):  # функция: если папки не существует, то создаем
    if not os.path.exists(path):
        os.mkdir(path)

def create_starter(dir_path, dir_name, folders): #создаем функцию, чтобы была возможность менять имена папок под конкретный проект
    full_path = os.path.join(dir_path, dir_name) #путь, где папка будет создана
    create_folder(full_path)
    for f in folders:
        folder = os.path.join(full_path, f) #аналогично для вложенных папок
        create_folder(folder)


if __name__ == "__main__":
    create_starter()

""" Проверяем модуль
from task_7_1 import create_starter

dir_path = r'C:\Games'
dir_name = 'my_project2'
folders = [
    'settings',
    'mainapp',
    'adminapp',
    'authapp'
]
create_starter(dir_path, dir_name, folders)"""