'''
Home work for Lesson 6
Exercise 3
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода
с учетом премии (get_total_income). Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
'''


class Worker:
    name = ''
    surname = ''
    position = ''
    _income = {'salary': None, 'bonus': None}

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return f'Имя сотрудника: {self.name} {self.surname}'

    def get_total_income(self):
        return f'Общий доход: {sum(self._income.values())} рублей'


name = input('Введите имя сотрудника: ')
surname = input('Введите фамилию сотрудника: ')
position = input('Введите должность сотрудника: ')
while True:
    try:
        salary = float(input('Введите ежемесяную заработную плату сотрудника: '))
        break
    except ValueError as err:
        continue

while True:
    try:
        bonus = float(input('Введите ежемесячную премию сотрудника: '))
        break
    except ValueError as err:
        continue


t_income = {"salary": salary, "bonus": bonus}
p = Position(name, surname, position, t_income)
print()
print(p.get_full_name())
print(p.get_total_income())
