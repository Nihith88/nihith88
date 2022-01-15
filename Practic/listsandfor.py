# practica
spisok = []
i = 0
print('Соревнования по Python')
kolvo = int(input('Введите колиество участников: \n'))
for i in range(kolvo):
    mesto = kolvo - i
    name = input(('Введите имя участника занявшего %d место:' % (mesto)))
    spisok.append(name)
    i =+ 1
print('Наши участники: ', sorted(spisok))
spisok.reverse()
result = spisok [:3]
print('Победители, занявшие призовые места:\n')
print(result[0], ' - 1 место', result[1], ' - 2 место', result[2], ' - 3 место. Поздравляем!')