my_list = [3, 7, 16, 1, 4, 2, 12, 56, 32]
my_new = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(f'Исходный список {my_list}')
print(f'Новый список {my_new}')
