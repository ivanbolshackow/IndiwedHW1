class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width


class Waight(Road):

    def __init__(self, _length, _width, heft, cm):
        super().__init__(_length, _width)
        self.heft = heft
        self.cm = cm

    def mas_2(self):
        return self._length * self._width * self.heft * self.cm


mas = Waight(20, 5000, 25, 5)
print(f'Вес асфальта {mas.mas_2() / 1000} тонн')