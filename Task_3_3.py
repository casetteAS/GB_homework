# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# Например:
# >>>  thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"], "П": ["Петр"]
# }
# Подумайте: полезен ли будет вам оператор распаковки? Как поступить, если потребуется сортировка по ключам?
# Можно ли использовать словарь в этом случае?

def thesaurus(*args):
    dict_names = {}
    first_letter = []
    for i in args:
        first_letter.append(i[0])
    first_letter.sort()

    for letter in first_letter:
        list_names = []
        for name in args:
            if name[0] == letter:
                list_names.append(name)
        dict_names.setdefault(letter, list_names)
    print(dict_names)
thesaurus('Kate','Klara','Jessy','Jerar','Alex')
