seasons = {'зима': (1, 2, 12),
           'весна': (3, 4, 5),
           'лето': (6, 7, 8),
           'осень': (9, 10, 11)}

month = int(input('Введите месяц числом: '))
for key in seasons.keys():
    if month in seasons[key]:
        print(key)