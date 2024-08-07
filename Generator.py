import rules
import blur_types

import numpy as np
import scipy.signal
from random import randint

# field = np.array([rules.chances[randint(0, len(rules.chances) - 1)] for x in range(rules.height * rules.width)]).reshape(rules.width, rules.height)


def Shuffle_field(field: np.ndarray, cell_type: list, field_types: set, chance: int):
    '''Функция случайного создания элементов типов, указанных в {cell_type}, на поле из элементов, указанных в {field_types}, с шансом {chance} (от 0 до 10)'''

    for y in range(rules.height):
        for x in range(rules.width):
            # maybe 100?
            if field[y][x] in field_types and randint(1, 10) <= chance:
                field[y][x] = cell_type[randint(0, len(cell_type) - 1)]
    return field


# def NarrowingTheField(new_field):
#     '''Функция для сужения поля чисел на 1 элемент с каждой стороны'''
#     field = np.zeros((rules.height, rules.width), dtype="int32")
#     for y in range(rules.height):
#         for x in range(rules.width):
#             field[y][x] = new_field[y + 1][x + 1]
#     return field


def FieldExpansion(field: np.ndarray):
    '''Функция для расширения поля чисел на 1 элемент с каждой стороны'''

    new_field = np.zeros((rules.height + 2, rules.width + 2), dtype="int32")
    for y in range(rules.height):
        new_field[y + 1][0] = field[y][0]
        new_field[y + 1][rules.width + 1] = field[y][rules.width - 1]
        for x in range(rules.width):
            new_field[y + 1][x + 1] = field[y][x]
    for x in range(rules.width):
        new_field[0][x + 1] = field[0][x]
        new_field[rules.height + 1][x + 1] = field[rules.height - 1][x]
    new_field[0][0] = field[0][0]
    new_field[0][rules.width + 1] = field[0][rules.width - 1]
    new_field[rules.height + 1][0] = field[rules.height - 1][0]
    new_field[rules.height + 1][rules.width +
                                1] = field[rules.height - 1][rules.width - 1]
    return new_field


def Blur(field: np.ndarray, blur_type=blur_types.standart, field_types={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}):
    '''Функция для размытия поля чисел'''

    # blur_matrix = [[ # 5x5
    #     [0.000789, 0.006581, 0.013347, 0.006581, 0.000789],
    #     [0.006581, 0.054901, 0.111345, 0.054901, 0.006581],
    #     [0.013347, 0.111345, 0.225821, 0.111345, 0.013347],
    #     [0.006581, 0.054901, 0.111345, 0.054901, 0.006581],
    #     [0.000789, 0.006581, 0.013347, 0.006581, 0.000789]
    # ]]

    blur_matrix = blur_type

    extended_field = FieldExpansion(field)
    new_field = np.ones((rules.height, rules.width), dtype="int32")

    for y0 in range(rules.height):
        for x0 in range(rules.width):
            if field[y0][x0] not in field_types:
                new_field[y0][x0] = field[y0][x0]
                continue
            counter = 0
            for y, x in rules.standart3x3:
                counter += extended_field[y0 + y +
                                          1][x0 + x + 1] * blur_matrix[y + 1][x + 1]
            # new_field[y0][x0] = int(counter) # баг с округлением в разных матрицах размытия
            new_field[y0][x0] = round(counter)

    return new_field


def Neighborhood(field: np.ndarray, x0: int, y0: int, cell_type: int, neighborhood_type):
    '''Функция для подсчёта числа соседей определенного типа (cell_type) в окрестности (neighborhood_type) у заданной клетки'''

    counter = 0
    for y, x in neighborhood_type:
        x += x0
        y += y0
        if x < 0 or x >= rules.width or y < 0 or y >= rules.height:
            continue
        if field[y][x] == cell_type:
            counter += 1
    return counter


def InitializeField(chances, shape):
    return np.random.choice(chances, size=shape).astype("int32")


def UpdateField(field: np.ndarray, cell_type: int, field_type: int, kernel: np.ndarray) -> None:
    '''
    Обновление поля по заданным параметрам

    Параметры
    ---------
    field: np.ndarray
        Исходное поле. По сути просто numpy матрица, в которой хранятся целые числа.
    cell_type: int
        Те числа (клетки), которые следует считать "живыми"
    field_type: int
        Те числа (клетки), которые следует считать "мёртвыми"
    iterations: int
        Количество итераций
    kernel: np.ndarray
        Правило соседства, а вообще - матрица свёртки.
        А точнее, квадратная матрица нечётных размеров,
        где единицей помечена клетка, которую стоит учитывать,
        а ноликом, которую не стоит учитывать.
    '''

    cell_mask = (field == cell_type)
    neighbors = scipy.signal.convolve2d(
        cell_mask, kernel, mode='same', boundary='wrap')

    # Применяем правила рождения и выживания
    birth_mask = (field == field_type) & \
        np.isin(neighbors, rules.Birth[cell_type])

    survival_mask = (field == cell_type) & \
        np.isin(neighbors, rules.Survive[cell_type])

    # Обновляем сетку
    new_field = field.copy()
    new_field[birth_mask] = cell_type
    new_field[~survival_mask & cell_mask] = field_type

    return new_field


def RunAutomaton(field: np.ndarray, cell_type: int, field_type: int, iterations: int, kernel: np.ndarray) -> None:
    '''
    Запуск клеточного автомата.

    Параметры
    ---------
    field: np.ndarray
        Исходное поле. По сути просто numpy матрица, в которой хранятся целые числа.
    cell_type: int
        Те числа (клетки), которые следует считать "живыми"
    field_type: int
        Те числа (клетки), которые следует считать "мёртвыми"
    iterations: int
        Количество итераций
    kernel: np.ndarray
        Правило соседства, а вообще - матрица свёртки.
        А точнее, квадратная матрица нечётных размеров,
        где единицей помечена клетка, которую стоит учитывать,
        а ноликом, которую не стоит учитывать.
    '''
    # import matplotlib.pyplot as plt

    # plt.figure(figsize=(6, 6))
    # plt.ion()
    
    for _ in range(iterations):
        # plt.imshow(field, cmap='tab10')
        # plt.draw()
        # plt.pause(0.001)
        # plt.clf()
        field = UpdateField(field, cell_type, field_type, kernel)
    
    # plt.ioff()
    # plt.imshow(field, cmap='tab10')
    # plt.show()

    return field