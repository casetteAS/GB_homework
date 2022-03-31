# 5. **(вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было
# задать имя обоих исходных файлов и имя выходного файла. Проверить работу скрипта.

import sys
from itertools import zip_longest

users, hobby, users_hobby = sys.argv[1:]
with open(users_hobby, 'w', encoding='utf-8') as f:
    with open(users, encoding='utf-8') as users:
        with open(hobby, encoding='utf-8') as hobby:
            num_users = sum(1 for line in users)
            num_hobbies = sum(1 for line in hobby)
            if num_users < num_hobbies:
                exit(1)
            users.seek(0)
            hobby.seek(0)
            for line_user, line_hobby in zip_longest(users, hobby):
                f.write(f'{line_user.strip()}: {line_hobby.strip() if line_hobby is not None else line_hobby}\n')

# python task_6_5.py "users.csv.txt" "hobby.csv.txt" "users_hobby_1.txt"