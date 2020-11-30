'''
Home work for Lesson 5
Exercise 7
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
'''

import json
i = 0
avg_profit = 0
firm_dict = {}
avg_dict = {}
my_list = list()
with open('firms.txt', 'r') as f_rnum:
    for line in f_rnum:
        name, ownership, income, expenses = line.split()
        profit = float(income) - float(expenses)
        firm_dict[name] = profit  # создаем словарь для каждой компании
        if profit >= 0:
            i += 1
            avg_profit += profit

    if i > 0:
        avg_profit = avg_profit/i  # считаем среднюю прибыль
    avg_dict["average_profit"] = avg_profit
    my_list.append(firm_dict)
    my_list.append(avg_dict)
    print(my_list)

with open("firms.json", "w") as f_wnum:
    json.dump(my_list, f_wnum)
