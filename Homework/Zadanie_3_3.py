"""Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
name - строка полученная от пользователя,
health = 100,
damage = 50. Поэкспериментируйте с значениями урона и жизней по желанию. ### Теперь надо создать функцию
attack(person1, person2). Примечание: имена аргументов можете указать свои. ### Функция в качестве аргумента
будет принимать атакующего и атакуемого. ### В теле функция должна получить параметр damage атакующего и отнять это
количество от health атакуемого. Функция должна сама работать со словарями и изменять их значения.
"""
# Исходные данные от пользователя
"""a = 1
name = input('Кто ты, Воин? ')
arm_class = float(input('А броня какого класса на тебе? (от 0 до 10):  '))
arm_class = (arm_class / 10) + 1
hero = {'calling': name, 'health': 100, 'damage': 40, 'armour': arm_class}
enemy = {'calling': 'Enemy', 'health': 100, 'damage': 40, 'armour': 1.4}
"""
# Объявим функцию махача:
def battle(hero, enemy):
   # Пока жив герой
   while True: # Цикл выполняется покуда дышат оба
        uron1 = hero['damage'] / enemy['armour']  # Урон 1
        print(hero['calling'], 'наносит удар с уроном ', round(uron1, 0))
        enemy['health'] = enemy['health'] - round(uron1, 0)
        print(enemy['calling'], 'получил урон ', round(uron1, 0), ', осталось ', enemy['health'], 'здоровья')
        if enemy['health'] <= 0:
            print(enemy['calling'], 'мертв. Победил', hero['calling'])
            print('Можете забрать доспехи ', enemy['calling'])
            break
    # Пока жив враг
        uron2 = enemy['damage'] / hero['armour']
        print(enemy['calling'], 'наносит удар с уроном ', round(uron2, 0))
        hero['health'] = hero['health'] - round(uron2, 0)  # Ответный удар
        print(hero['calling'], ', ты получил урон ', round(uron2, 0), ', осталось ', hero['health'], 'здоровья')
        if hero['health'] <= 0:
            print(hero['calling'], ', ты мертв. Победил', enemy['calling'])
            print(enemy['calling'], 'забрал всё ваше снаряжение')
            break

a = 1
while a != '0':
    name = input('Кто ты, Воин? ')
    arm_class = float(input('А броня какого класса на тебе? (от 0 до 10):  '))
    arm_class = (arm_class / 10) + 1
    hero = {'calling': name, 'health': 100, 'damage': 40, 'armour': arm_class}
    enemy = {'calling': 'Enemy', 'health': 100, 'damage': 40, 'armour': 1.4}
    battle(hero, enemy)
    a = (input('В бой? (введите enter для продолжения, 0 для завершения:  '))
