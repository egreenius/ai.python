'''
Homework for Lesson 3

Exercise 2.
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
'''


def user_profile(f_name, l_name, dob, city, email, phone):
    '''
    Возвращает строку с данными профиля пользователя

    :param f_name: str
    :param l_name: str
    :param dob: str
    :param city: str
    :param email: str
    :param phone: str
    :return: str
    >> user_profile('Александр', 'Пушкин', '1801', 'Санкт Петербург', 'Нет', 'Нет')
    Имя:Александр, Фамилия: Пушкин, ДР: 1801, Город: Санкт Петербург, Email: Нет , Телефон: Нет
    '''
    profile = f'Имя:{f_name}, Фамилия: {l_name}, ДР: {dob}, Город: {city}, Email: {email}, Телефон: {phone}'
    return profile


def user_profile2(**kwargs):
    '''
    Возвращает словарь именованных аргументиов, переданных в функцию

    :param kwargs: dict
    :return: dict
    '''
    return kwargs


my_fname = input('Введите Ваше имя: ')
my_lname = input('Введите Вашу фамилию: ')
my_dob = input('Введите дату Вашего рождения: ')
my_city = input('Введите Ваш город рождения: ')
my_email = input('Введите Ваш адрес эл. почты: ')
my_phone = input('Введите Ваш телефон: ')

u_profile = user_profile(l_name=my_lname, f_name=my_fname, dob=my_dob, phone=my_phone, email=my_email, city=my_city)
print('Вы ввели: ', u_profile)
print()

u_profile2 = user_profile2(lname=my_lname, fname=my_fname)  # используем часть именованных аргументов
print('Ввели только именованные переменные: ', u_profile2)
print()

profile_dict = {}  # объявляем пустой словарь
profile_dict['Имя'] = my_fname
profile_dict['Фамилия'] = my_lname
profile_dict['Дата рождения'] = my_dob
u_profile2 = user_profile2(**profile_dict)  # передача значений словаря в функцию
print('Выводим ввиде словаря: ', u_profile2)  # вывод значения функции в виде словаря
print()

user_data = ''  # вывод данных о пользователе одной строкой, распаковка из словаря
for key in u_profile2.keys():
    user_data = f' {user_data}{key}: {u_profile2.get(key)}, '
print('Выводим ввиде сформированной строки: ', user_data)
