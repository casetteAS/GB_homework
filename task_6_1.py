# 6.1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов
# web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
#
# [
# ...
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# ...
# ]
#
# Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
data = []
with open('nginx_logs.txt', encoding='utf-8') as f:
    # print(f.read())
    for number, row in enumerate(f):
        splited_row = row.split() # Получаем список
        result = [splited_row[0], splited_row[5][1:], splited_row[6]]
        data.append(tuple(result))
        if number == 15: # можно использовать для сохранения памяти
            break
print(data)
