""" В этой игре человек загадывает число, а компьютер пытается его угадать.
В начале игры человек загадывает число от 1 до 100 в уме или записывает его на листок бумаги. Компьютер начинает его
отгадывать предлагая игроку варианты чисел. Если компьютер угадал число, игрок выбирает “победа”. Если компьютер назвал
 число меньше загаданного, игрок должен выбрать “загаданное число больше”. Если компьютер назвал число больше,
 игрок должен выбрать “загаданное число меньше”. Игра продолжается до тех пор пока компьютер не отгадает число.

"""
import random
minn = 1
maxx = 100
compnumber = random.randint(minn, maxx)
while True:
    print("Это число {} ?" .format(compnumber))
    hint = input('Подсткажите: ваше число больше (>), меньше (<) или равно (любой символ)?  ')
    if hint == '<':
        maxx = compnumber - 1
        compnumber = random.randint(minn, maxx)
    elif hint == '>':
        minn = compnumber + 1
        compnumber = random.randint(minn, maxx)
    else:
        print("Какой я умный, я угадал ваше число {}!!!" .format(compnumber))
        break