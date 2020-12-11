'''
Home work for Lesson 8
Exercise 1
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.

Интересное решение в разборе. Обрати внимание на объявление типа данных date с кавычками!
https://www.youtube.com/watch?v=69yXmArAvz0&ab_channel=Luchanos
'''


class Date:
    __day = int
    __month = int
    __year = int

    def __init__(self, date_str):  # идея - сначала проверяем вхолные данные, потом присваиваем атрибутам класса
        if not Date.is_valid(date_str):
            raise ValueError('Дата введена некорректно', date_str)
        Date.convert(date_str)

    def __str__(self):
        return f'Вы ввели дату: день - {self.__class__.__day}, месяц - {self.__class__.__month}, год - {self.__class__.__year}'

    @classmethod
    def convert(cls, date_str):
        day, month, year = date_str.split('-')
        cls.__day = int(day)
        cls.__month = int(month)
        cls.__year = int(year)
        return cls.__day, cls.__month, cls.__year

    @staticmethod
    def is_valid(date_str):
        dict_t = {"day": 1, "month": 1, "year": 2000}
        date_dict = {k: int(v) for k, v in zip(dict_t.keys(), date_str.split('-')) if v.isdigit()}
        if not date_dict.keys() == dict_t.keys():  # если где-то было введено не число, структуры словарей не совпадут
            return False

        if date_dict['month'] < 1 or date_dict['month'] > 12 or date_dict['year'] < 0:
            return False  # Предположим что год не может быть меньше 0

        d = 0 if date_dict['year'] % 4 else 1
        valid_days = [31, 28 + d, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if date_dict['day'] < 1 or date_dict['day'] > valid_days[date_dict['month'] - 1]:
            return False
        return True


my_date_str = "29-02-2001"  # некорректное значение дня в феврале
try:
    my_data = Date(my_date_str)
    print(my_data)
except ValueError as err:
    print(err)

my_date_str = "32-01-2001"  # некорректное значение дня в январе
try:
    my_data = Date(my_date_str)
    print(my_data)
except ValueError as err:
    print(err)

my_date_str = "01-13-2001"  # некорректное значение месяца в году
try:
    my_data = Date(my_date_str)
    print(my_data)
except ValueError as err:
    print(err)

my_date_str = "01-may-2001"  # некорректное значение месяца в текстовом формате
try:
    my_data = Date(my_date_str)
    print(my_data)
except ValueError as err:
    print(err)

a = Date.convert('29-11-2020')  # вызов напрямую класс-метода.
print(type(a), a)

a = Date('29-11-2020')
a.convert('30-11-2020')  # убеждаемся что класс-метод меняет значения защищенных (приватных) аттрибутов. Опасно как то!
print(a)
print('Проверяем работу статического метода: ', a.is_valid('30-11-2020'))

while True:  # можно поиграть с датами
    my_date_str = input('Задайте дату в формате dd-mm-yyyy:')
    if my_date_str == '':  # если нажать Ввод, то выйдем из цикла
        break
    try:
        my_data = Date(my_date_str)
        print(my_data)
    except ValueError as err:
        print(err)
