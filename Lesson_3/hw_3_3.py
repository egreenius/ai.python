'''
Homework for Lesson 3

Exercise 3.
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
'''


def sum_max2(arg1, arg2, arg3):
    '''
    Возвращает сумму наибольших двух аргументов

    :param arg1: any type
    :param arg2: any type
    :param arg3: any type
    :return: any
    '''
    l = list(locals().values())  # получаем список значений аргументов
    max1 = max(l)  # находим первый максимальный аргумент
    l.remove(max(l))  # удаляем первый максимальный аргумент
    max2 = max(l)  # находим следующий максимальный аргумент
    return max1 + max2


def sum_max21(*args):
    '''
    Принимает любое количество позицицонных аргументов
    и возвращает сумму двух наибольших

    :param args:
    :return:
    '''
    l = list(args)  # получаем список значений аргументов
    max1 = max(l)
    l.remove(max(l))
    max2 = max(l)
    return max1 + max2


print('Сумма наибольших числе: ', sum_max2(2, 3, 5))  # аргументы числа
print('Сумма наибольших строк: ', sum_max2('пять', 'два', 'три'))  # аргуименты строки
print('Сумма наибольших булевых выражений: ', sum_max2(True, False, True))
print()
print(sum_max21(2, 4, 5, 7, 9, 3))
