'''
Home work for Lesson 7
Exercise 2
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
'''

from abc import abstractmethod, ABC
from random import randint, randrange
from functools import reduce


class Clothes(ABC):

    @abstractmethod
    def t_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def t_consumption(self):
        return self.size / 6.5 + 0.5

    # def sum_cons(self, other):
    #     return Coat(self.t_consumption + other.t_consumption)

    def __str__(self):
        return f'{self.size}'


class Suite(Clothes):
    def __init__(self, height):
        self.heigth = height

    @property
    def t_consumption(self):
        return self.heigth * 2 + 0.3

    # def __add__(self, other):
    #     self.t_consumption = self.t_consumption + other.t_consumption
    #     return Suite(self)

    def __str__(self):
        return f'{self.heigth}'


#  Вариант 1. Создаем коллекцию экземпляров одежды каждого вида, используя list comprehension
my_suite_list = [Suite(randrange(140, 200, 2)) for _ in range(0, randint(0, 10))]
t_suite_cons = 0
for el in my_suite_list:
    print(f'Рост костюма: {el}. Расход ткани на костюм {el.t_consumption:.2f}')
    t_suite_cons += el.t_consumption
print(f'Расход ткани на костюмы = {t_suite_cons:.2f}')

my_coat_list = [Coat(randrange(44, 60, 2)) for _ in range(0, randint(0, 10))]
t_coat_cons = 0
for el in my_coat_list:
    print(f'Размер пальто: {el}. Расход ткани на пальто {el.t_consumption:.2f}')
    t_coat_cons += el.t_consumption
print(f'Расход ткани на пальто = {t_coat_cons:.2f}')

print(f'Общий расход ткани: {(t_suite_cons/100 + t_coat_cons):.2f}')

с = reduce(Suite.custom_sum, my_suite_list)
print(c)
# if len(my_suite_list) == 1:
#     a = my_suite_list[0].t_consumption
# else:
#    a = reduce(lambda x, y: x+y, my_suite_list)
# a = reduce(my_suite_list.sum_cons, my_suite_list)
print(f'Расход ткани на костюмы = {a:.2f}')

for el in my_coat_list:
    print(f'Размер пальто: {el}')
# if len(my_coat_list) == 1:
#     b = my_coat_list[0].t_consumption
# else:
    b = reduce(lambda x, y: x.property+y.property, my_coat_list)
print(f'Расход ткани на пальто = {b}')

# my_coat_list = [Coat(randrange(44, 60, 2)).t_consumption for _ in range(0, 2)]
# my_fabric_consumption = reduce(lambda x.t_consumtion, y.t_consumption: x.t_consumtion+y.t_consumtion, my_suite_list)
