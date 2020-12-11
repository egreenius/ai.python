'''
Home work for Lesson 2
'''
'''
Exercise 1
1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
'''
my_list = [1, 2, 3, 4]
my_tuple = (5, 6, 7, 8, 9)
my_complex_list = ['моя строка', 9, 3.1415, 0, None, my_list, False, my_tuple]
for i in range(len(my_complex_list)):
    print(i, type(my_complex_list[i]))
'''
Exercise 2
2. Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
'''
user_input = input('Введите данные Вашего списка через запятую: ')
user_list = user_input.split(',')
print('Ваш список: ', user_list)
for i in range(len(user_list)):  # можно использовать также такую идею: for i in range(1, len(user_list), 2):
    if i % 2 != 0:
        user_list[i-1], user_list[i] = user_list[i], user_list[i-1]
print('Наш список: ', user_list)

'''
Exercise 3
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
'''
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
seasons = [winter, spring, summer, autumn]
seasons_names = ['winter', 'spring', 'summer', 'autumn']

while True:  # Организуем бесконечный цикл для пользовательского ввода
    user_month = input('Введите номер месяца в году от 1 до 12: ')
    try:  # вставляем перехват ошибок
        if int(user_month) in months:
            break
    except ValueError as err:
        print('Вы ввели строку: ', user_month)
        continue

# Case 1. Use type "list" only
for i in seasons:
    if int(user_month) in i:
        print(f'Your month {user_month} in season {seasons_names[seasons.index(i)]}')

# Case 2. Use  dict type only
season_dict = {12: "Winter", 1: "Winter", 2: "Winter", 3: "Spring", 4: "Spring", 5: "Spring", 6: "Summer", 7: "Summer", 8: "Summer", 9: "Autumn", 10: "Autumn", 11: "Autumn"}
print(f'Your month {int(user_month)} in {season_dict.get(int(user_month))}')

# Case 3. Use  list and dict types together.  This is most relevant solution, imho
season_dict2 = {tuple(winter): "Winter", tuple(spring): "Spring", tuple(summer): "Summer", tuple(autumn): "Autumn"}
for i in seasons:
    if int(user_month) in i:
        print(f'Your month {user_month} in season {season_dict2.get(tuple(i))}.')

'''
Exercise 4
4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
'''
user_input = input('Введите строку из нескольких слов: ')
user_list = user_input.split(' ')
for i in user_list:
    print(f'{user_list.index(i)} :  {i[:9]}')

'''
Exercise 5
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы
с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2]
'''
my_rates = [7, 5, 3, 3, 2]
print(f'Текущий рейтинг {my_rates}')
while True:  # Организуем бесконечный цикл для пользовательского ввода
    u_vote = input('Оцените нашу работу: ')
    try:  # вставляем перехват ошибок
        u_vote = int(u_vote)  # если данное преобразование закончится ошибкой, значит пользователь ввел не целое число
        break
    except ValueError as err:
        print(f'Вы ввели строку: {u_vote}. Введите целое число')
        continue
for rate in my_rates:  # должно работать следующее: i = 0 (for n in my_rates: if rate <= n i+=1) my_rates.insert(i, rate)
    if u_vote > rate:
        my_rates.insert(my_rates.index(rate), u_vote)
        break
    if my_rates.index(rate) == len(my_rates) - 1:
        my_rates.append(u_vote)
        break
print(f'Новый рейтинг {my_rates}')
'''
Exercise 6
6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. 
Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара 
и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения). 
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, 
например название, а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
'''
list_of_goods = []  # инициализируем пустой список
goods = {}  # объявляем пустой словарь - будущая карточка товара
i = 0
while True:  # Организуем цикл для ввода данных о товаре
    print('Введите информацию о товаре:')
    goods_name = input(' Введите название товара: ')
    goods['Название'] = goods_name

    while True:  # Организуем бесконечный цикл для ввода цены товара
        goods_price = input(' Введите цену товара: ')
        try:  # вставляем перехват ошибок
            goods_price = float(goods_price)  # если данное преобразование закончится ошибкой, значит пользователь ввел не целое число
            if goods_price < 0:
                print('Вы ввели отрицательное число : ', goods_price)
                continue
            break
        except ValueError as err:
            if not goods_price:  # проверка на пустое значение строки. Согласно PEP-8 пустые последовательности (строки, списки, кортежи) ) являются "ложными"
                print('Вы ввели пустую строку: <пусто>')
            else:
                print('Вы ввели строку: <', goods_price, '>вместо положительного числа')
            continue
    goods['Цена'] = goods_price

    while True:  # Организуем бесконечный цикл для ввода количества товара
        goods_quantity = input(' Введите количество товара: ')
        try:  # вставляем перехват ошибок
            goods_quantity = int(goods_quantity)  # если данное преобразование закончится ошибкой, значит пользователь ввел не целое число
            if goods_quantity < 0:
                print('Вы ввели отрицательное число: ', goods_quantity)
                continue
            break
        except ValueError as err:
            if not goods_quantity:  # проверка на пустое значение строки. Согласно PEP-8 пустые последовательности (строки, списки, кортежи) ) являются "ложными"
                print('Вы ввели пустую строку: <пусто>')
            else:
                print('Вы ввели строку: <', goods_quantity, '>вместо количества товара')
            continue
    goods['Количество'] = goods_quantity

    goods_unit = input(' Введите единицу измерения: ')
    goods['Единица измерения'] = goods_unit
    i += 1
    goods_id = (i, {**goods})  # формируем список (кортеж) из карточек товаров. Разгружаем туда словарь, наче после очистки данные сотрутся
    list_of_goods.append(goods_id)
    goods.clear()
    is_finish = input('Чтобы продолжить ввод информации о следующем товаре нажмите ВВОД. Чтобы закончить, нажмите ПРОБЕЛ и ВВОД: ')
    if is_finish.lower() == ' ':
        break
    else:
        continue
print(list_of_goods)  # собрали информацию о списке товаров
analytics = {}  # инициализируем пустой словарь для сбора аналитики
attr_list = []  # инициализируем пустой список аттрибутов товаров
l = list_of_goods[0]  # получаем первый элемент списка - кортеж
list_of_keys = l[1].keys()  # получаем список ключей - аттрибутов карточки товара
for k in list_of_keys:  # делаем обход по ключам
    for g in list_of_goods:  # делаем обход по списку товаров
        attr_list.append(g[1].get(k))  # формируем список аттрибутов всех товаров по заданному ключу
    analytics[k] = attr_list.copy()  # формируем словарь "ключ : список аттрибутов товаров". Копируем сформированный список
    attr_list.clear()  # очищаем сформированный список аттрибутов перед следующей итерацией цикла
print(analytics)
