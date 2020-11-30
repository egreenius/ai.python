'''
Home work for Lesson 5
Exercise 3
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
'''

with open('staff_list.txt', 'r') as my_file:
    i = 0
    print('Список сотруников с заработной платой < 20,000 рублей: ')
    for el in [line for line in my_file if float(line.split()[1]) < 20000]:
        print(el, end='')
    print('Средняя величина дохода сотрудников организации составляет: ')
    ave_inc = 0
    my_file.seek(0)
    for line in my_file:
        i += 1
        ave_inc += float(line.split()[1])
    ave_inc = ave_inc/i
    print(f'{ave_inc:.2f}')
