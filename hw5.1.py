filename = input("Придумайте название файла: ")
print("Чтобы выйти, оставьте пустую строку: ")
my_list = []
while True:
    text = input("Введите текст: ")
    if text == '':
        print(my_list)
        exit()
    else:
        newline = text + '\n'
        my_list.append(newline)

    with open("filename", "w") as file:
        file.writelines(my_list)
