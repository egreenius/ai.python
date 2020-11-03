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

'''
Exercise 2
'''
print('Завершение программы')
