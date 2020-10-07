number = input("Введите число: ")
x = 0
for i in number:
    while int(i) > x:
        x = int(i)
print(x)
