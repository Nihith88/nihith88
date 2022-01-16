"""Работа с типом данных словарь
тип данных dict - неупорядоченная коллекция производльных объектов с доступом по ключу
my_dict = {key1: val1, key2: val2....keyn:
Основные действия: получение элемента по ключу perem = my_dict[key1]
Добавление значения friend['hascar'] = True
Изменение значения friend['hascar'] = False
Удаление значения в словаре remove friend['nation']
оператор in     'age' in friend
Перебор словая циком for: по ключам, for key in dict.keys()
по значениям,
по паре ключ-значение

"""
solders = {'zvanie': 'Ефрейтор', 'name': 'Василий', 'age': 31, 'nation': 'русский', 'profy': True}

for key in solders.keys():  # Перебор словаря по ключам. Указывать метод .keys при этом не обязательно
    print(key, (solders[key]))
print('============')
for val in solders.values(): # Перебор словаря по значениям
    print(val)
print('============')
for item in solders.items(): # Перебор сразу по ключу и значению кортежами.
    print(item)
print('============')
for key,val in solders.items(): # Перебор по ключу и значениям с разбитием кортежа на переменные
    print (key, val)
