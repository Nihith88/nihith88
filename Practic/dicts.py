"""Работа с типом данных словарь

"""
solders = {'zvanie': 'Ефрейтор', 'name': 'Василий', 'age': 31, 'nation': 'русский', 'profy': True}

for key in solders.keys():  # Перебор словаря по ключам. Указывать метод .keys при этом не обязательно
    print(key, (solders[key]))
for val in solders.values(): # Перебор словаря по значениям
    print(val)
for item in solders.items(): # Перебор сразу по ключу и значению кортежами.
    print(item)
for key,val in solders.items(): # Перебор по ключу и значениям с разбитием кортежа на переменные
    print (key, val)
