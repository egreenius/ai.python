'''
Homework for Lesson 3

Exercise 1.
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''


def division_function(dividend, denominator):  # можно сразу использовать блок try ... except ...
    '''
    Возвращает частное от деления двух аргументов

    :param dividend:
    :param denominator:
    :return: число = результат деления или строку, если делитель = 0
    '''
    if denominator == 0:
        return "Делитель не может быть равен нулю"
    return dividend/denominator


def input_float(invite_str):
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


def input_float2(invite_string):
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


num_1 = input_float2('Введите число, которое хотите разделить: ')
num_2 = input_float2('Введите число, на которое хотите разделить: ')
result = division_function(num_1, num_2)
while type(result) is str:
    print(result)
    num_2 = input_float2('Введите число, на которое хотите разделить: ')
    result = division_function(num_1, num_2)

print(f'Частное от деления {division_function(num_1, num_2):.2f}')
