'''
Home work for Lesson 7
Exercise 1
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.

Разбор домашки здесь:
https://www.youtube.com/watch?v=eR_zw40xtvc&ab_channel=Luchanos
'''


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        my_str = str()
        max_1 = len(str(max(max(self.matrix))))  # вычисляем максимальный элемент матрицы и находим его длину
        for raw in self.matrix:
            for el in raw:
                my_str = f'{my_str}{(max_1 - len(str(int(el))) + 1) * " "}{el:.2f}'  # форматируем строку матрицы
                # в зависимости от длины максимального элемента матрицы
            my_str = my_str + '\n'  # добавляем перевод строки для перехода к выводу следующей строки маьтрицы
        return my_str

    def dimension(self):
        row = len(self.matrix)
        col = len(self.matrix[0])
        return row, col

    # def __add__(self, other):  # вариант перегрузки метода __add__ с испольлзованием метода списка append (код ниже)
    #     # Николай, какой из методов лучше?
    #     if type(other) == Matrix:  # проверяем что класс складываемых объектов одинаковый
    #         raw, col = self.dimension()
    #         raw_o, col_o = other.dimension()
    #         if raw != raw_o or col != col_o:
    #             raise ValueError('Both matrix must have the same dimension.')
    #
    #         new_matrix = []
    #         for i in range(raw):
    #             new_matrix.append([])
    #             for j in range(col):
    #                 new_matrix[i].append(self.matrix[i][j] + other.matrix[i][j])
    #         return Matrix(new_matrix)
    #     elif type(other) == int or type(other) == float:
    #         raw, col = self.dimension()
    #         new_matrix = self.matrix.copy()
    #         for i in range(raw):
    #             for j in range(col):
    #                 new_matrix[i][j] = self.matrix[i][j] + other
    #         return Matrix(new_matrix)
    #     else:
    #         raise ValueError('Unsupported type for matrix add: ', type(other))


    def __add__(self, other):  # вариант перегрузки метода с созданием нового списка такой же структуры
        if type(other) == Matrix:  # проверяем что класс складываемых объектов одинаковый
            raw, col = self.dimension()
            raw_o, col_o = other.dimension()
            if raw != raw_o or col != col_o:
                raise ValueError('Both matrix must have the same dimension.')

            new_matrix = [[0] * col for _ in range(raw)]  # а можно было создать новую матрицу как строчкой ниже
            #  new_matrix = self.matrix.copy()             # new_matrix = self.matrix.copy() - какой вариант лучше?
            for i in range(raw):
                for j in range(col):
                    new_matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
            return Matrix(new_matrix)
        elif type(other) == int or type(other) == float:
            raw, col = self.dimension()
            new_matrix = self.matrix.copy()
            for i in range(raw):
                for j in range(col):
                    new_matrix[i][j] = self.matrix[i][j] + other
            return Matrix(new_matrix)
        else:
            raise ValueError('Unsupported type for matrix add: ', type(other))


my_nested_list = [[1.0567, 3, 5, 78], [45, 2, 90, 3], [461, 0, 121, 534]]
my_nested_list_2 = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
my_nested_list_3 = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
my_matrix = Matrix(my_nested_list)
print(my_matrix)

my_matrix_2 = Matrix(my_nested_list_2)
print(my_matrix_2)

my_matrix_3 = Matrix(my_nested_list_2)
print(my_matrix_3)

my_new_matrix = my_matrix + my_matrix_2 + my_matrix_3
print(my_new_matrix)

my_new_matrix_1 = my_matrix + 7
print(my_new_matrix_1)
