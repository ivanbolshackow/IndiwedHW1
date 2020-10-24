firm = {'Иван': 23003, 'Ольга': 25312, 'Виктор': 19432, 'Анна': 18755, 'Дмитрий': 22658}
try:
    file_obj = open("test_3.txt", 'w', encoding="utf-8")
    for last_name, salary in firm.items():
        file_obj.write(last_name + ':' + str(salary) + "\n")
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    file_obj.close()
summa = 0
count = 0
persons = []
with open("test_3.txt", "r", encoding="utf-8") as file_obj:
    for line in file_obj:
        print(line, end="")
        tokens = line.split(':')
        if int(tokens[1]) <= 20000:
            persons.append(tokens[0])
        summa += int(tokens[1])
        count += 1
result = summa / count
print(f"Не достигли нужного оклада: {persons}")
print(f"Средний доход: {result}")