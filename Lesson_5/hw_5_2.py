'''
Home work for Lesson 5
Exercise 2

2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
'''

with open('my_first_file.txt', 'r') as my_file:  # используем файл из предыдущего упражнения
    i = 0
    for line in my_file:
        i += 1
        print(f'Cтрока {i}. Количество слов в строке: {len(line.split())}')
    print('Всего строк в файле: ', i)