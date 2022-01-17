# ПРОВЕРКА ВИСОКОСНОСТИ ГОДА
year = 2019
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    isvis = True
else:
    isvis = False