from itertools import zip_longest

with open('users_hobby.txt', 'w', encoding='utf-8') as f:
    with open('users.csv.txt', encoding='utf-8') as users:
        with open('hobby.csv.txt', encoding='utf-8') as hobby:
            num_users = sum(1 for line in users)
            num_hobbies = sum(1 for line in hobby)
            if num_users < num_hobbies:
                exit(1)
            users.seek(0)
            hobby.seek(0)
            for line_user, line_hobby in zip_longest(users, hobby):
                f.write(f'{line_user.strip()}: {line_hobby.strip() if line_hobby is not None else line_hobby}\n')


with open('users_hobby.txt', 'r', encoding='utf-8') as f:
    print(f.read())
