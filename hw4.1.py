from sys import argv

file_name, hour, rate, benefit = argv

calculation = (int(hour) * int(rate)) + int(benefit)
print(f"Заработная плата сотрудника: {calculation}")
