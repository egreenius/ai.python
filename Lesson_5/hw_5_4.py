'''
Home work for Lesson 5
Exercise 4
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''


my_dict = {"One": 'Один', "Two": 'Два', "Three": 'Три', "Four": 'Четыре'}
with open('e_numerals.txt', 'r') as f_enum, open('r_numerals.txt', 'w') as f_rnum:
    for line in f_enum:
        m_l = line.split(' ')
        m_l[0] = my_dict.get(m_l[0])
        m_s = ' '.join(m_l)
        f_rnum.write(m_s)
with open('e_numerals.txt', 'r') as f_enum, open('r_numerals.txt', 'r') as f_rnum:
    print('Исходный файл:')
    for line in f_enum:
        print(line, end='')
    print('\nПреобразованный файл:')
    for line in f_rnum:
        print(line, end='')