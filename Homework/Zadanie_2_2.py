"""Дана дата в формате dd.mm.yyyy, например: 02.11.2013. Ваша задача — вывести дату в текстовом виде,
   например: второе ноября 2013 года. Склонением пренебречь (2000 года, 2010 года)

"""
ddate = input('Введите дату в формате ДД.ММ.ГГГГ:  ')
# ==== объявление словарей дней и месяцев ====
days = {'01': 'первое', '02': 'второе', '03': 'третье', '04': 'четвертое', '05': 'пятое', '06': 'шестое',
        '07': 'седьмое', '08': 'восьмое', '09': 'девятое', '10': 'десятое', '11': 'одиннадцатое', '12': 'двенадцатое',
        '13': 'тринадцатое', '14': 'четырнадцатое', '15': 'пятнадцатое', '16': 'шестнадцатое', '17': 'семнадцатое',
        '18': 'восемнадцатое', '19': 'девятнадцатое', '20': 'двадцатое', '200': 'двадцать',
        '30': 'тридцатое', '300': 'тридцать'}
months = {'01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля', '05': 'мая', '06': 'июня', '07': 'июля',
          '08': 'августа', '09': 'сентября', '10': 'октября', '11': 'ноября', '12': 'декабря'}
# Проверим что ввел пользователь, если некорректно, то запрос даты заново:
if int(ddate[:2]) > 30 and (ddate[3:5] in ('04', '06', '09', '11')):   # Проверка корректности дня для 30-дн месяцев
    ddate = input('Дата некорректна, проверьте день и введите снова в верном формате ДД.ММ.ГГГГ:')
elif (int(ddate[:2]) > 29) and ddate[3:5] == '02':  # Проверка корректности для февраля. Вис. год не учитываем
    ddate = input('Дата некорректна, проверьте день и введите снова в верном формате ДД.ММ.ГГГГ:')
while (ddate[:2] not in days.keys() and 32 < int(ddate[:2])) or ddate[3:5] not in months.keys() or not ddate[6:10].isdigit():
    ddate = input('Дата некорректна, введите снова в верном формате ДД.ММ.ГГГГ:')
else:  # Если все в порядке, то начинаем выборку
    dd = ddate[:2]      # Срез по дню
    mm = ddate[3:5]     # Срез по месяцу
    year = ddate[6:10]  # Срез по году
    if dd in days.keys():
        worddate = days[dd]
    elif 20 < int(dd) < 30:
        newday = int(dd) - 20
        newkeyday = ('0' + str(newday))
        worddate = str(days['200']) + ' ' + str(days[newkeyday])
    elif 31 > int(dd) > 30:
        newday = int(dd) - 30
        newkeyday = ('0' + str(newday))
        worddate = str(days['300']) + ' ' + str(days[newkeyday])

    if mm in months.keys():
        worddate = str(worddate) + ' ' + str(months[mm])
    worddate = worddate + ' ' + year
    print('Прописной формат даты: {} года.'.format(worddate))
