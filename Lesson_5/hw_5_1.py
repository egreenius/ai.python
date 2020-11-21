'''
Home work for Lesson 5
Exercise 1

1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
'''
from datetime import datetime

# открываем два файла на запись, каждый раз заново.
with open('my_first_file.txt', 'w') as my_file, open('my_second_file.txt', 'w') as my_sfile:
    my_file.write(str(datetime.now()) + '\n')  # запись с помощью метода write()
    my_file.write('...\n')
    print(str(datetime.now()), file=my_sfile)  # запись с помощью функции print()
    while True:
        m_f = input('Увековечьте свои мысли! Как поток закончится, нажмите Ввод: ')
        if m_f == '':
            my_file.write('...\n')
            print('...', file=my_sfile)
            break
        my_file.write(m_f + '\n')
        print(m_f, file=my_sfile)
# открываем два файла на чтение, выводим сожержимое на экран
with open('my_first_file.txt', 'r') as my_file, open('my_second_file.txt', 'r') as my_sfile:
    print(f'Ваши замечательные мысли из файла {my_file.name} от: ')
    for line in my_file:
        print(line, end='')  # функция print вызыввется с подавлением паразитного перевода строки.
    print(f'Ваши замечательные мысли из файла {my_sfile.name} от: ')
    for line in my_sfile:
        print(line, end='')  # функция print вызыввется с подавлением паразитного перевода строки.
