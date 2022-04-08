import re

look_for = re.compile(r'(^\S+)[\s-]*\[(\S+\s+\+\d+)\]\s*\"(\w+)\s*(\S+)\s*\S*\s*(\d+)\s*(\d+)')

file = open('nginx_logs.txt', encoding='Latin-1')
text = file.read()
result = re.findall(look_for, text)
print(result)
#если нужно пройти по всем записям, то:
# file_1 = open('nginx_logs.txt', encoding='Latin-1')
# text_1 = file_1.readlines()
# for t in text_1:
#     print(re.findall(look_for, t))