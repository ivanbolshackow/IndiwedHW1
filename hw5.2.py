my_list = ["python\n", "best\n", "of\n", "the\n", "best\n"]
with open("test_2.txt", "w+", encoding="utf-8") as file_obj:
    file_obj.writelines(my_list)
with open("test_2.txt") as file_obj:
    lines = 0
    letters = 0
    for line in file_obj:
        lines += line.count("\n")
        letters = len(line)-1
        print(f"{letters} Букв в строке.")
    print(f"Количество строк: {lines}")
