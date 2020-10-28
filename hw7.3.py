class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __str__(self):
        return f"{self.cell}"

    def __add__(self, other):
        return Cell(self.cell + other.cell)

    def __sub__(self, other):
        if self.cell - other.cell > 0:
            return Cell(int(self.cell - other.cell))
        else:
            return f'Число меньше 0'

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __truediv__(self, other):
        return Cell(self.cell // other.cell)

    def make_order(self, line):
        return "".join("*" if i % line != 0 or i % self.cell == 0 else "*\n" for i in range(1, self.cell + 1))


cell_1 = Cell(12)
cell_2 = Cell(4)

print("Сумма:", cell_1 + cell_2)
print("Вычитание:", cell_1 - cell_2)
print("Умножение:", cell_1 * cell_2)
print("Деление:", cell_1 / cell_2)
print(cell_1.make_order(4))
