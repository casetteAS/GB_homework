''' 1. Написать функцию email_parse(<email_address>), которая при помощи регулярного
выражения извлекает имя пользователя и почтовый домен из email адреса и возвращает их в
виде словаря. Если адрес не валиден, выбросить исключение ValueError. Пример:
#>>> email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
#>>> email_parse('someone@geekbrainsru')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
...
raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru
Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном
выражении; имеет ли смысл в данном случае использовать функцию re.compile()?
'''
import re
def email_parse(email,):
    dict_email_parse = {}
    look_for_name = r'^[\w._-]+'
    look_for_domain = r'@[A-Za-z]+\.[\w.-]+'
    result_name = re.findall(look_for_name, email)
    for item in result_name:
        dict_email_parse['username'] = item
    result_domain = re.findall(look_for_domain, email)
    for item in result_domain:
        dict_email_parse['domain'] = item

    return dict_email_parse

print(email_parse('someone-ak.sdf@geekbrains.us.com'))