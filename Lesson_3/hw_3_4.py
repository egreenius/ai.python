'''
Homework for Lesson 3

Exercise 4.
4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде
функции my_func(x, y). При решении задания необходимо обойтись без встроенной функции возведения числа
в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
'''


def my_exp(x, y):  # вариант реализации с использоанием **
    '''
    Возвращает результат возвделения числа X в степень Y
    
    :param x: number > 0
    :param y: int < 0
    :return: number
    
    '''
    if x <= 0:  # проверка входных параметров
        err = 'Первый агумент должен быть положительным'
        return err
    if y >= 0:  # проверка входных параметров
        err = 'Второй агумент должен быть отрицательным'
        return err
    return x**y


def my_exp2(x, y):  # вариант реализации с использоанием рекурсии
    '''
    Возвращает результат возвделения числа X в степень Y

    :param x: number > 0
    :param y: int < 0
    :return: number

    '''
    if x <= 0:  # проверка входных параметров
        err = 'Первый агумент должен быть положительным'
        return err
    if y >= 0:  # проверка входных параметров
        err = 'Второй агумент должен быть отрицательным'
        return err

    if abs(y) == 1:
        return 1/x
    else:
        return 1/x * my_exp2(x, y + 1)


def my_exp3(x, y):  # вариант реализации с использоанием цикла
    '''
    Возвращает результат возвделения числа X в степень Y

    :param x: number > 0
    :param y: int < 0
    :return: number

    '''
    if x <= 0:  # проверка входных параметров
        err = 'Первый агумент должен быть положительным'
        return err
    if y >= 0:  # проверка входных параметров
        err = 'Второй агумент должен быть отрицательным'
        return err

    res = 1 / x
    while abs(y) > 1:
        res = res * 1/x
        y = y + 1
    return res


def input_float(invite_str):  # базовая функция ввода действительных чисел
    '''
    Возвращает числовое значение, введенное пользователем

    ('Введите число: ') -> number, если введено число
    ('Введите число: ') -> string, если введено не число
    :return: или число, или ошибку Error
    >> input_float('Введите число: ') - 5
    5.00
    >> input_float('Введите число: ') - пять
    <Error description>
    '''
    var_number = input(invite_str)
    try:  # вставляем перехват ошибок
        var_number = float(var_number)  # если данное преобразование c ошибкой, значит пользователь ввел не число
        return var_number
    except ValueError as err:
        return err


def input_float2(invite_string):  # функция ввода действительных чисел - "пока не введешь правильно"
    '''
    Возвращает число, введенное пользователем

    :param invite_string: str
    :return: number (float)
    '''
    while True:  # Организуем бесконечный цикл для пользовательского ввода
        num = input_float(invite_string)
        if type(num) is not ValueError:
            break
        print('Вы ввели не число. ', num)
        continue
    return num


def input_int(invite_str):  # базовая функция ввода целых чисел
    '''
    Возвращает числовое значение, введенное пользователем

    ('Введите целое число: ') -> integer, если введено число
    ('Введите целое число: ') -> string, если введено не число
    :return: или целое число, или ошибку Error
    >> input_int('Введите целое число: ') - 5
    5
    >> input_int('Введите целое число: ') - пять
    <Error description>
    '''
    var_number = input(invite_str)
    try:  # вставляем перехват ошибок
        var_number = int(var_number)  # если данное преобразование c ошибкой, значит пользователь ввел не число
        return var_number
    except ValueError as err:
        return err


def input_int2(invite_string):  # функция ввода целых чисел - "пока не введешь правильно"
    '''
    Возвращает целое число, введенное пользователем

    :param invite_string: str
    :return: number (integer)
    '''
    while True:  # Организуем бесконечный цикл для пользовательского ввода
        num = input_int(invite_string)
        if type(num) is not ValueError:
            break
        print('Вы ввели не целое число. ', num)
        continue
    return num


while True:  # организуем ввод чисел согласно условияю задачи
    my_num = input_float2('Введите положительное число: ')
    if my_num > 0:
        break

while True:   # организуем ввод чисел согласно условияю задачи
    my_int = input_int2('Введите целое отрицательное число: ')
    if my_int < 0:
        break

print(my_exp(my_num, my_int))  # вызов первого варианта реализации
print(my_exp2(my_num, my_int))  # вызов второго варианта реализации, с рекурсией
print(my_exp3(my_num, my_int))  # вызов второго варианта реализации, с циклом
