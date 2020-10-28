from random import randint

my_list = [randint(2, 18) for i in range(10)]
my_new = [el for el in my_list if my_list.count(el) < 2]
print(f'рандомные числа: {my_list}')
print(f'Без повторяющихся чисел: {my_new}')
