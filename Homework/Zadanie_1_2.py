"""Используя цикл, запрашивайте у пользователя число, пока оно не станет больше 0, но меньше 10.
   После того, как пользователь введет корректное число, возведите его в степень 2 и выведите на экран.

"""
number = float(input('Введите число от 0 до 10: \n'))
while number < 0 or number > 10: #пока число не соответствует диапазону
    print ('Число ', number, 'вне диапазона') #выводим сообщение что число вне диапазона
    number = float(input('Введите повторно число от 0 до 10: \n')) # и запршиваем число заново
else:
    print ("Число корректное, результат операции:", number**2)