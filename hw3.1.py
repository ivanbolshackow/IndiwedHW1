def div():
    try:
        arg1 = int(input("Введите первое число: "))
        arg2 = int(input("Введите второе число: "))
        res = arg1 / arg2
    except ValueError:
        return 'Введите число!'
    except ZeroDivisionError:
        return "Вы ввели неправильно число, Оно должно быть больше 0."
    return res


print(f'Рузультат: {div()}')
