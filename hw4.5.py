from functools import reduce


def my_func(s_1, el):
    return s_1 * el


print(f'Четные числа: {[el for el in range(99, 1001) if el % 2 == 0]}')
print(f'Произведение всех чисел: {reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0])}')
