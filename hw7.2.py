class Clothed:
    def __init__(self, size, height):
        self.size = size
        self.height = height

    def get_square_c(self):
        return self.size / 6.5 + 0.5

    def get_square_j(self):
        return self.height * 2 + 0.3

    @property
    def get_sq_full(self):
        return str(f'Общая площадь ткани: '
                   f' {(self.size / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Coat(Clothed):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.square_c = round(self.size / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь на пальто: {self.square_c}'


class Jacket(Clothed):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.square_j = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Площадь на костюм: {self.square_j}'


coat = Coat(1, 3)
jacket = Jacket(2, 4)
print(coat)
print(jacket)
print(coat.get_sq_full)
print(jacket.get_sq_full)
