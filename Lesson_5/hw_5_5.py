'''
Home work for Lesson 5
Exercise 5
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''


from functools import reduce

my_str = '1 2 3 4 5 6 7 8 9'
my_str = input(' Введите числа, разделенные пробелом: ')
with open('write_numbers.txt', 'w') as f_wnum:
    print(my_str, file=f_wnum)
    print(my_str, file=f_wnum)  # пишем вторую строку в файле



with open('write_numbers.txt', 'r') as f_rnum:
    sum = 0
    for line in f_rnum:  # исходим из предположения, что строка в файле может быть не одна
        m_s = line.split()
        for i in range(len(m_s)):
            sum += float(m_s[i])
    print(sum)  # первый линейный вариант решения

    f_rnum.seek(0)  # возвращаем курсор на начало файла
    a = [x.split() for x in f_rnum]  # получаем список, содержащий строки файла, разбитые на символы разделенные пробелом
    print(reduce(lambda x, y: float(x) + float(y), reduce(lambda x, y: x+y, a)))  # правый reduce собирает список в одну строку, второй считает сумму
