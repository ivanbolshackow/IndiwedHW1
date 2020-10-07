a = int(input("Введите сколько вы пробежали км за день: "))
b = int(input("Введите сколько в общем км вы хотите пробежать: "))

resuly_days = 1
resuly_km = a
while resuly_km < b:
    a = a + a * 0.1
    resuly_days += 1
    resuly_km = resuly_km + a
    print(f"Вы достигнете цели на %d день" % resuly_days)
