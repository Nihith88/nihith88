"""
 функции sorted, filter, map

"""
# sorted - сортировка последовательности sorted(iterable, *, key=None, reverse=False) - последовательность, ключ для
# сортировки, порядок
a = [1, 5, 3, 8, 4, 8, 3, 8, 8, 0, 99, 4]
print(sorted(a))  # можем сортировать набор строк, кортежей и т.д.
print(sorted(a, reverse=True))
cities = [('Moscow', 10000), ('London', 9254), ('Zamascus', 5000)]
print(sorted(cities))  # Сортировка по умолчанию по первому элементу в кортеже (элементе списка)


def by_pop(city):  # объявим функцию для сортировки по второму элементу кортежа
    return city[1]  # функция возвращает аргументу значение второго элемента


print(sorted(cities, key=by_pop))  # функция указывается в качестве ключа для сортировки, либо
print(sorted(cities, key=lambda city: city[1]))  # c использованим анонимной функции

# FILTER - фильтрация последовательности filter(функция, последовательность)
nums = (1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)


def is_even(number):  # Фильтр последовательности через объявление функции
    return number % 2 == 0

res = filter(is_even, nums)
print(res) # результат - адрес памяти
print(list(res))

result = filter(lambda numm: numm % 2 == 0, nums)  # либо использованием анонимной функции
print(list(result))

names = ('Kate', 'Igorr', 'Joe', 'Ray', 'Larry')

def long_names(name):  # Функция для фильтрации строки по длине
    return len(name) > 3

newlist = filter(long_names, names)  # c использованием написаной функции
print(list(newlist))

newlist2 = filter(lambda name: len(name) > 3, names)  # Через анонимную функцию
print(list(newlist2))

# Функция МАР - применение функции к каждому элементу последовательности maf(func, iterable)

print(list(map(lambda n: n**2, a)))  # Возвести каждый элемент последовательности в квадрат
print(list(map(lambda n: str(n), a)))  # Перевести каждый элемент последовательности в строку

