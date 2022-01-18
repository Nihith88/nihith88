""" Функция в Python сама по себе тоже является объектом. Мы можем записать этот объект в некторую переменную
ФУНКЦИЮ МОЖНО ПЕРЕДАВАТЬ ПАРАМЕТРОМ В ДРУГИЕ ФУНКЦИИ
Lambda используется для создания анонимных функций по месту их использования lambda вх.парам: результат
lambda number: number % 2 == 0
"""


def f():
    print('some text')


def to(f_param):
    f_param()


to(f)


def myfilter(numbers):
    result = []  # результатом выполнения функции будет список
    for number in numbers:
        if number % 2 == 0:
            result.append(number)
    return result


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 25]
print(myfilter(numbers))
