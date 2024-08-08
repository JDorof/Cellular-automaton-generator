import rules
import blur_types

import numpy as np
import scipy.signal
from random import randint


def Shuffle_field(field: np.ndarray, cell_type: list, field_types: set, chance: int):
    '''Функция случайного создания элементов типов, указанных в {cell_type}, на поле из элементов, указанных в {field_types}, с шансом {chance} (от 0 до 10)'''

    for y in range(rules.height):
        for x in range(rules.width):
            # maybe 100?
            if field[y][x] in field_types and randint(1, 10) <= chance:
                field[y][x] = cell_type[randint(0, len(cell_type) - 1)]
    return field


def Blur(field: np.ndarray, blur_type: np.ndarray, field_types: set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}) -> np.ndarray:
    '''Функция для размытия поля чисел'''

    mask = np.isin(field, list(field_types))
    new_field = scipy.signal.convolve2d(field, blur_type, mode='same', boundary=rules.boundary)
    new_field[~mask] = field[~mask]

    return np.round(new_field).astype(int)


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
        cell_mask, kernel, mode='same', boundary=rules.boundary)

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

