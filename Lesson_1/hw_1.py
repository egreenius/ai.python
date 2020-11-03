'''
Home work for Lesson 1
'''
'''
Exercise 1
'''
var_1 = 'Give me answer'
var_2 = 42
var_3 = 'What is the question?'
var_4 = '- Let me think...'

print(var_1)
print(var_2)
print(var_3, var_4)
# Пользователю нужно ввести число
while True: # Организуем бесконечный цикл для пользовательского ввода
    var_number = input('Введите число: ')
    try:  # вставляем перехват ошибок
        float(var_number) # если данное преобразование закончится ошибкой, значит пользователь ввел не число
        print('Вы ввели число: ', var_number)
        break
    except ValueError:
        print('Вы ввели строку: ', var_number)
        continue
print('Завершение задачи №1')
'''
Exercise 2
'''
# Пользователь вводит число, мы интерпретируем число как секунды, и выводим в формате "чч:мм:сс"
while True: # Организуем бесконечный цикл для пользовательского ввода
    var_number = input('Введите целое количество секунд: ')
    try:  # вставляем перехват ошибок
        var_number = int(var_number) # если данное преобразование закончится ошибкой, значит пользователь ввел не целое число
        if var_number < 0:
            print('Вы ввели отрицательное число: ', var_number)
            continue
        print('Вы ввели количество секунд равное: ', var_number)
        break
    except ValueError:
        if not var_number:
            print('Вы ввели пустую строку: <пусто>')
        continue

print('Вы ввели строку: ', var_number)
hour = var_number // 3600
minute = var_number % 3600//60
second = var_number % 60
time = f"{hour:02}:{minute:02}:{second:02}"
print("Ваше время: ", time)

print('Завершение задачи №2')

print('Завершение программы')
