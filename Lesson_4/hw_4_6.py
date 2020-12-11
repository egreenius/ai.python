'''
Home work for Lesson 4
Exercise 6
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание,
что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

'''

from itertools import count
from itertools import cycle

start_list = int(input('Введите целое число - начало списка: '))
end_list = int(input('Введите целое число - конец списка: '))
for el in count(start_list):  # для себя - посмотри что делает count в itertools
    if el > end_list:
        break
    else:
        print(el)
print()
c = 1
i = 0
a = input('Введите элементы списка через пробел: ').split(' ')
for el in cycle(a):
    i += 1
    if c > 2:
        break
    elif i % len(a) == 0:
        c += 1  # увеличиваем счетчик копирования, только после того как все элементы списка были скопированы
    print(el)
