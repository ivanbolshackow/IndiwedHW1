profit = (input("Введите выручку фирмы: "))
costs = (input("Введите издержки фирмы: "))
if profit > costs:
    prf = profit - costs
    print(f"Ваша прибыль составила: {prf}")
    worker = int(input("Введите количество работников: "))
    print(f"Прибиль на одного работника составила {prf / worker}")
elif profit == costs:
    print("Ваша фирма работает в ноль.")
elif costs > profit:
    cst = costs - profit
    print(f"Ваша фирма сработала в убыток :- {cst}")
