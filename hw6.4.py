class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} Стартовала'

    def stop(self):
        return f'{self.name} Остановилась'

    def turn_right(self):
        return f'{self.name} Повернула на право'

    def turn_left(self):
        return f'{self.name} повернул на лево'

    def show_speed(self):
        return f'Текущая скорость {self.name} составляет {self.speed} км/ч'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость городского автомобмля {self.name} {self.speed} км/ч')

        if self.speed > 60:
            return f'скорость машины {self.name} превышает разрешенную скорость городского автомобиля'
        else:
            return f'скорость машины {self.name} в пределах разрешенной городской скорости'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость рабочий машины {self.name} составляет {self.speed} км/ч')

        if self.speed > 40:
            return f'скорость машины {self.name} превышает разрешенную скорсоть рабочей машины'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} Полицейская машина'
        else:
            return f'{self.name} Не полицейская машина'


audi = SportCar(130, 'Синий', 'Ауди', False)
nissan = TownCar(47, 'Черный', 'Ниссан', False)
volkswagen = WorkCar(55, 'Красный', 'Фольчваген', False)
ford = PoliceCar(110, 'Белый', 'Форд', True)
print(nissan.turn_left())
print(f'{audi.go()} со скоростью: \n {audi.show_speed()}')
print(f'У {volkswagen.name} {volkswagen.color} цвет кузова')
print(f'{audi.name} полицейская машина? {audi.is_police}')
print(nissan.show_speed())
print(f'{ford.name}  полицейская машина? {ford.is_police}')
print(ford.show_speed())
print(f' {ford.turn_right()}, {audi.stop()}')
print(volkswagen.show_speed())
print(f'У {audi.name} {audi.color} цвет кузова')
