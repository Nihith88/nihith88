"""Работа с типом данных множества
Тип данных МНОЖЕСТВА (Set) - неупорядоченные коллекции, содержащие неповторяющиеся элементы
mno = {v1, v2, v3}
Действия со множествами: Добавление элемента mno.add('value')
                         Удаление элемента mno.remove('value')
                         длина множества len
                         in, for
                         работа с несколькими множествами (объединение, пересечение, разность)

"""
# cities = {'Moscow', 'Paris', 'Kabul', 'Tokyo'}
cities = ('Moscow', 'Paris', 'Kabul', 'Tokyo', 'Moscow')  # Объявим список
cities = set(cities)  # Переведем список в тип множество, будет сохранен только последний повторяющийся элемент
print(cities)
cities.add('Berlin')  # Добавление элемента в множество (удаление cities.remove)

for city in cities: # Перебор элементов множества
    print(city)

# Операции со множествами
me = {'hammer', 'saw', 'nail', 'drill', 'spoon'}
she = {'spoon', 'lipstick', 'soap', 'drill', 'fork'}
print(me | she)  # Объединим два множества
print(me & she)  # Найдем пересечения множеств (элементы, которые есть в обоих множествах)
print(me - she)  # Элементы которые не повторяются в втором множестве

