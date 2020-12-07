'''
Homework for Lesson 3

Exercise 6.
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
'''

def int_func(l_text):
    return l_text.title()  # правильнее использовать capitalize


user_str = input('Введите строку со словами латиницей: ')
user_list_str = user_str.split(' ')
my_list = list()
for word in user_list_str:
    my_list.append(int_func(word))  # можно было через map реализовать

my_str = ' '.join(my_list)

print('Исходная строка:', user_str)
print('Преобразованная строка', my_str)

my_func = lambda u_str: u_str.title()
print('Преобразованная неименованной функцией', my_func(user_str))

#  попробовать через bytearray