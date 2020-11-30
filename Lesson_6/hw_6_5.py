'''
Home work for Lesson 6
Exercise 5
5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и
метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''


class Stationery:
    title = str()

    def draw(self):
        print(f'Запуск отрисовки с помощью {self.title}')


class Pen(Stationery):
    def __init__(self):
        self.title = "Pen"

    def draw(self):
        print(f'Рисует {self.title}')


class Pencil(Stationery):
    def __init__(self):
        self.title = "Pencil"

    def draw(self):
        return f'Рисует {self.title}'  # у данного класса метод draw возвращает строку


class Handle(Stationery):
    def __init__(self, color=None):
        self.color = color
        self.title = "Marker"

    def draw(self, color):
        super().draw()  # наследуем родительскую функциональность
        self.color = color
        print(f'{self.title} color is {self.color}')


my_pen = Pen()
my_pen.draw()
my_pencil = Pencil()
print(my_pencil.draw())
my_pen.draw()

my_handle = Handle()
my_handle.draw('Red')
