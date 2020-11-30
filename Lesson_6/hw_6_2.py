'''
Home work for Lesson 6
Exercise 2
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
'''


class Road:
    _length = 0
    _width = 0

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_calc(self, density, thick):
        return self._length * self._width * density * thick


u_road = input('Введите длину и ширину дороги в метрах через пробел: ')
u_road_thick = input('Введите плотность асфальта в кг/кв.м и высоту асфальта в см через пробел: ')
l, w = u_road.split()
d, t = u_road_thick.split()

r = Road(int(l), int(w))
m = r.mass_calc(int(d), int(t))
print(f'Масса асфальта: {m//1000} т')
