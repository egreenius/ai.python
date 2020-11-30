'''
Home work for Lesson 6
Exercise 4
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
'''


class Car:
    speed = 0
    color = "red"
    name = "Ford"
    is_police = False

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self, speed):
        self.speed = speed
        print(f'The {self.color} one {self.name} is going with speed: {self.speed} km/h')

    def stop(self):
        if self.speed > 0:
            self.speed = 0
            print(f'The {self.color} one {self.name} has stopped')

    def turn(self, direction):
        if self.speed > 0:
            print(f'The {self.color} one {self.name} turn {direction}')

    def show_speed(self):
        print(f'The {self.color} one {self.name} has speed: {self.speed} km/h')


class TownCar(Car):
    def show_speed(self):  # полностью переопределяем метод, без сохранения родительской функциональности
        if self.speed > 60:
            print(f'The {self.color} one {self.name} speed exceed 60 km/h')
        else:
            print(f'The {self.color} one {self.name} has speed: {self.speed} km/h')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):  # переопределяем метод, но не полностью, наследуем функциональность от родителя
        super().show_speed()
        if self.speed > 40:
            print(f'The {self.color} one {self.name} speed exceed 40 km/h')


class PoliceCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed, is_police=True)

    def show_speed(self):
        if self.is_police:
            print(f'The {self.color} one {self.name} has no speed limit')


print('Используем стандартный класс Car')
my_car = Car("Ford", "red", 60)
my_car.go(40)
my_car.stop()
my_car.go(20)
my_car.turn("left")
my_car.show_speed()
print()
print('Исполльзуем дочерний класс SportCar')
my_sportcar = SportCar("Ferrari", "red", 120)
my_sportcar.show_speed()
my_sportcar.stop()
my_sportcar.go(60)
my_sportcar.turn("right")
my_sportcar.show_speed()
print()
print('Используем дочерний класс TownCar')
my_towncar = TownCar("Nissan", "white", 60)
my_towncar.show_speed()
my_towncar.stop()
my_towncar.go(65)
my_towncar.turn("Left")
my_towncar.show_speed()
print()
print('Используем дочерний класс WorkCar')
my_workcar = WorkCar("Honda", "grey", 60)
my_workcar.show_speed()
my_workcar.stop()
my_workcar.go(40)
my_workcar.turn("Right")
my_workcar.show_speed()
print()
print('Используем дочерний класс PoliceCar')
my_policecar = PoliceCar("Crown Victoria", "police", 100)
my_policecar.show_speed()
my_policecar.stop()
my_policecar.go(40)
my_policecar.turn("Left")
my_policecar.show_speed()
