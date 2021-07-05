class Car:

    def __init__(self, color, name, is_police: bool = False):
        self.color = color
        self.name = name
        self.is_police = True if is_police else False
        self.speed = 0
        self._direction = ' '

    def go(self, speed):
        self.speed = speed

    def stop(self):
        self.speed = 0
        print('Автомобиль остановился.')

    def turn(self, direction):
        self._direction = direction

    def show_speed(self):
        print(f'Скорость автомобиля {self.speed} км/ч')

    @property
    def direction(self):
        return self._direction


class TownCar(Car):

    _max_granted_speed = 60

    def __init__(self, *args):
        super().__init__(*args)

    def show_speed(self):
        super().show_speed()
        if self.speed > self._max_granted_speed:
            print('Превышение скорости!')


class SportCar(Car):
    def __init__(self, *args):
        super().__init__(*args)


class WorkCar(Car):
    _max_granted_speed = 40

    def __init__(self, *args):
        super().__init__(*args)

    def show_speed(self):
        super().show_speed()
        if self.speed > self._max_granted_speed:
            print('Превышение скорости!')


class PoliceCar(Car):
    def __init__(self, *args):
        super().__init__(*args, is_police=True)


if __name__ == '__main__':
    cars_data = {
        ('Чёрный', 'VW Tiguan'): TownCar,
        ('Жёлтый', 'Lamborghini'): SportCar,
        ('Синий', 'Reno'): WorkCar,
        ('Серый', 'UAZ'): PoliceCar,
    }

    for car_descr, car_cls in cars_data.items():
        car = car_cls(*car_descr)

        print(f'Марка автомобиля: {car.name}.')
        print(f'Цвет автомобиля: {car.color}.')
        print(f'Является ли автомобиль полицейским: {car.is_police}.')
        print(f'Автомобиль завёлся и начал движение!')
        car.go(30)
        car.show_speed()
        car.go(45)
        car.show_speed()
        car.go(75)
        car.show_speed()
        car.turn('налево')
        print(f'Автомобиль повернул {car.direction}.')
        car.turn('направо')
        print(f'Автомобиль повернул {car.direction}.')
        car.stop()
        print('\n')
