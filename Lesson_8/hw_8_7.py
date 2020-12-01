'''
Home work for Lesson 8
Exercise 7
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные
числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата. '''


class ComplexNumber:
    re = float
    im = float

    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __add__(self, other):
        return ComplexNumber(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        return ComplexNumber(self.re * other.re - self.im * other.im, self.re * other.im + self.im * other.re)

    def __str__(self):
        return f'{self.re} {"+ " + str(self.im) if self.im >= 0 else "- " + str(abs(self.im))}i'


z1 = ComplexNumber(-4, 2)
z2 = ComplexNumber(1, 1)

z3 = z1 + z2


print(f'Результат сложения ({z1}) и ({z2}): = ', z3)
print(f'z1 + z2 = (z1.re + z2.re) + (z1.im + z2.im)i = {z3}')
print()
z4 = z1 * z2
print(f'Результат умножения ({z1}) и ({z2}): = ', z4)
print(f'z1 * z2 = (z1.re * z2.re - z1.im * z2.im) + (z1.re * z2.im + z1.im * z2.re)i = {z4}')

