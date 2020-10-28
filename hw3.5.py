def my_sum():
    sum_res = 0
    ex = True
    while ex == True:
        number = input("Введите число или Q для выхода: ").split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                ex = False
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Текущая сумма составляет: {sum_res}')
    print(f'Ваша общая сумма: {sum_res}')


my_sum()
