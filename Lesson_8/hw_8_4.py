'''
Home work for Lesson 8
Exercise 4
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных. Подсказка:
постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по
ООП.

Интересное использование множеств set() для хранения техники н складе в разборе
https://www.youtube.com/watch?v=69yXmArAvz0&ab_channel=Luchanos
'''

class WrongValue(Exception):
    def __init__(self, *args, **kwargs):
        self.text = args[0]


class Wirehouse:
    __storage = {}

    def take(self, device):
        device.department = 'WH'
        device_type = device.get_type()
        ls = self.__storage.get(device_type) or []
        ls.append(device)
        self.__storage[device_type] = ls

    def give_out(self, device_type, department):
        ls = self.__storage.get(device_type)
        if ls is None:
            raise KeyError('Device not found')  # проверяем, есть ли девайс запрошенного типа на складе
        #        res_list = []
        try:
            device = ls.pop()  # удаляем девайс из спика тем самым забираем девайс данного типа со склада.
            #  в переменной device - удаленный объект. То есть выдаем любой девайс заданного типа
        except IndexError as err:  # если нет больше девайсов данного типа на складе
            print(err)
        device.department = department  # присваиваем значение параметру, то есть теперь девайс находится
        # в этом департаменте
        return device

    def __str__(self):
        return str({k: len(self.__storage.get(k)) for k in self.__storage.keys()})


class OfficeEquipment:
    device_manufacture = str
    device_model = str
    serial_number = str
    inventory_number = str
    department = ''

    def __init__(self, device_manufacture, device_model, serial_number, inventory_number):
        self.device_manufacture = device_manufacture
        self.device_model = device_model
        self.serial_number = serial_number
        self.inventory_number = inventory_number

    @classmethod
    def get_type(cls):
        return cls.__name__

    def __str__(self):
        return f'{self.get_type()}: {self.device_manufacture}, {self.device_model}, ' \
               f'SN:{self.serial_number}, IN:{self.inventory_number}, Department: {self.department} '


class Printer(OfficeEquipment):
    iscolor = bool  # '''if False - black&white, if True - color'''
    speed = int  # '''speed - page per minute'''

    def __init__(self, device_manufacture, device_model, serial_number, inventory_number, speed, iscolor=False):
        super().__init__(device_manufacture, device_model, serial_number, inventory_number)
        if not type(speed) is int:
            raise WrongValue('Скорость печати должна быть целым числом', speed)
        self.speed = speed
        self.iscolor = iscolor


class Scanner(OfficeEquipment):
    size = str  # '''size is like A4, A5 and so on'''
    resolution = int  # '''resolution in DPI - dot per inch'''

    def __init__(self, device_manufacture, device_model, serial_number, inventory_number, size, resolution):
        super().__init__(device_manufacture, device_model, serial_number, inventory_number)
        if not type(resolution) is int:
            raise WrongValue('Разрешение сканирования должно быть целое число', resolution)
        self.size = size
        self.resolution = resolution


class CopyMachine(OfficeEquipment):
    size = str  # '''size is like A4, A5 and so on'''
    speed = int  # '''speed - page per minute'''

    def __init__(self, device_manufacture, device_model, serial_number, inventory_number, size, speed):
        super().__init__(device_manufacture, device_model, serial_number, inventory_number)
        if not type(speed) is int:
            raise WrongValue('Скорость копирования должна быть целым числом', speed)
        self.size = size
        self.speed = speed


print('Купили 2 принтера, сканер и ксерокс:')  # создаем три объекта по одному каждого типа
printer = Printer("HP", "DeskJet 3010", "123M345", "2020-11-30N123", 5)
printer2 = Printer("Samsung", "SM 6010", "456SM123-RU", "2020-11-30N126", 10)
scanner = Scanner("Microtek", "M2048", "23SN2020", "2020-11-30N124", "A4", 2400)
copy_machine = CopyMachine("Xerox", "Xerox - 348", "3450128NNN-02-RU", "2020-11-30N125", "A3", 20)
print(printer)
print(printer2)
print(scanner)
print(copy_machine)
print()

print('Принимаем купленные товары на склад: ')
wh = Wirehouse()  # создаем склад
wh.take(printer)  # приняли на склад принтер
wh.take(printer2)
wh.take(scanner)  # приняли на склад сканер
wh.take(copy_machine)  # приняли на склад ксерокс
print(wh)
print('Атрибуты устройств выглядят теперь так:')
print(printer)
print(printer2)
print(scanner)
print(copy_machine)
print()

my_dev = wh.give_out('Printer', 'HR')  # Выдали один принтер подразделдению HR
print('Состояние склада после выдачи одно принтера: ')
print(wh)
print('Состояние принтера после выдачи: ')
print(printer)
print(printer2)
wh.take(my_dev)  # принимаем этот принтер обратно на склад
print('Состояние склада после приема принтера обратно: ')
print(wh)
print('Состояние принтера после возврата его на склад: ')
print(printer)
print(printer2)
print()
print('Проверка работы собственных исключений:')
try:
    printer3 = Printer("Samsung", "SM 6010", "456SM123-RU", "2020-11-30N126", '')
except WrongValue as err:
    print(err)

try:
    scanner2 = Scanner("Microtek", "M2048", "23SN2020", "2020-11-30N124", "A4", '')
except WrongValue as err:
    print(err)

try:
    copier = CopyMachine("Xerox", "Xerox - 348", "3450128NNN-02-RU", "2020-11-30N125", "A3", '')
except WrongValue as err:
    print(err)