'''
Home work for Lesson 8
Exercise 2
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой.
'''


class ZeroDiv(Exception):
    def __init__(self, *args, **kwargs):
        self.text = args[0]


def div(x, y):
    if not y:
        raise ZeroDiv('На ноль делить нельзя')
    return x / y


while True:
    my_str = input('Введите делимое и делитель через пробел, или Ввод для завершения: ')
    if not my_str:
        break
    x, y = my_str.split(' ')
    try:
        print(f'{x}:{y} = {div(int(x), int(y)):.2f}')
    except Exception as err:
        print(err)
