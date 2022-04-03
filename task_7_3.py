'''3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
Написать скрипт, который собирает все шаблоны в одну папку templates, например:
|--my_project
   ...
  |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html
Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
(они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача,
которая решена, например, во фреймворке django.'''

import os
import shutil

def create_folder(path):
    if not os.path.exists(path):
        os.mkdir(path)
my_dir = 'task_7_3'
create_folder(my_dir)

files = []
root_dir = r'my_project'
for r, d, f in os.walk(root_dir):
    for file in f:
        if '.html' in file:
            files.append(os.path.join(r, file))

# print(files)
for path in files:
    folder = os.path.join(my_dir, os.path.basename(os.path.dirname(path)))
    create_folder(folder)
    save_path = os.path.join(folder, os.path.basename(path))
    # print(path)
    # print(save_path)
    shutil.copy(path, save_path)