import rules
import blur_types

import numpy as np
import scipy.signal

from random import randint, seed

# field = np.array([rules.chances[randint(0, len(rules.chances) - 1)] for x in range(rules.height * rules.width)]).reshape(rules.width, rules.height)

seed(a=rules.seed, version=2)
np.random.seed(seed=randint(0, 2^32 - 1))


def ReplaceCells(field: np.ndarray, replace: list, to: list, p: float = 1) -> np.ndarray:
    '''
    Функция случайной замены клеток типов из target_types на типы из replacement_types с заданной вероятностью.

    Parameters:
    - field: np.ndarray - Массив, в котором производится замена клеток.
    - replace: list - Список типов клеток, которые нужно заменить.
    - to: list - Список типов клеток, на которые будут заменены целевые клетки.
    - p: float - Вероятность замены клеток, значение от 0 до 1.

    Returns:
    - np.ndarray - Массив с замененными клетками.
    '''

    # Создаем маску для клеток, которые должны быть заменены
    mask = np.isin(field, replace)

    if np.any(mask):
        # Определяем, какие из клеток для замены будут заменены на новые типы с заданной вероятностью
        mask[mask] = np.random.choice(
            [False, True],
            p=[1 - p, p],
            size=mask.sum()
        )

        # Генерируем новые значения для замены
        field[mask] = np.random.choice(
            list(to),
            size=mask.sum()
        )

    return field


def Blur(field: np.ndarray, blur_type: np.ndarray, target_values: list = range(1, 11), iterations: int = 1) -> np.ndarray:
    '''
    Функция для размытия числового массива с сохранением значений, не входящих в список target_values.


    Параметры
    ---------
    - field: np.ndarray - Массив, который нужно размыть.
    - blur_type: np.ndarray - Ядро свертки для размытия.
    - target_values: list - Список значений, которые должны быть размыты. Значения, не входящие в этот список, остаются неизменными.
    - iterations: int - Количество итераций размытия.

    Возвращает
    ----------
    - np.ndarray - Массив после размытия.
    '''

    # Преобразуем target_values в множество для ускорения поиска
    target_values_set = set(target_values)

    for _ in range(iterations):
        # Создаем маску для клеток, которые нужно размыть
        blur_mask = np.isin(field, list(target_values_set))

        # Применяем размытие ко всему полю
        blurred_field = scipy.signal.convolve2d(field, blur_type, mode='same', boundary='wrap')

        # Восстанавливаем оригинальные значения на местах, которые не подлежат размытию
        blurred_field[~blur_mask] = field[~blur_mask]

        # Округляем значения и приводим их к целым числам
        field = blurred_field

    return np.round(field).astype(int)


def InitializeField(chances, shape):
    return np.random.choice(chances, size=shape).astype("int32")


def UpdateField(grid: np.ndarray, live_cell_value: int, dead_cell_value: int, neighborhood_kernel: np.ndarray) -> np.ndarray:
    '''
    Обновляет состояние клеток в поле по заданным правилам.

    Параметры
    ----------
    - grid: np.ndarray - Исходное поле, представляющее собой матрицу чисел.
    - live_cell_value: int - Значение, обозначающее "живую" клетку.
    - dead_cell_value: int - Значение, обозначающее "мертвую" клетку.
    - neighborhood_kernel: np.ndarray -
        Ядро свертки, определяющее соседство клеток.
        Квадратная матрица нечетных размеров, где единицы обозначают клетки,
        учитываемые при расчете соседства, а нули - не учитываемые.

    Возвращает
    ----------
    - np.ndarray - Обновленное поле.
    '''

    # Создаем маску для клеток, которые считаются "живыми"
    live_cell_mask = (grid == live_cell_value)

    # Применяем ядро свертки для подсчета соседей
    neighbor_counts = scipy.signal.convolve2d(live_cell_mask, neighborhood_kernel, mode='same', boundary='wrap')

    # Определяем маски для клеток, которые должны "родиться" и "выжить"
    birth_mask = (grid == dead_cell_value) & np.isin(neighbor_counts, rules.Birth[live_cell_value])
    survival_mask = (grid == live_cell_value) & np.isin(neighbor_counts, rules.Survive[live_cell_value])

    # Создаем копию поля для обновления
    updated_grid = grid.copy()

    # Обновляем состояния клеток
    updated_grid[birth_mask] = live_cell_value
    updated_grid[~survival_mask & live_cell_mask] = dead_cell_value

    return updated_grid


def RunAutomaton(grid: np.ndarray, live_cell_value: int, dead_cell_value: int, num_iterations: int, neighborhood_kernel: np.ndarray) -> np.ndarray:
    '''
    Запускает процесс клеточного автомата для заданного количества итераций.

    Параметры
    ----------
    grid: np.ndarray
        Исходное поле, представляющее собой матрицу чисел.
    live_cell_value: int
        Значение, обозначающее "живую" клетку.
    dead_cell_value: int
        Значение, обозначающее "мертвую" клетку.
    num_iterations: int
        Количество итераций для выполнения клеточного автомата.
    neighborhood_kernel: np.ndarray
        Ядро свертки, определяющее соседство клеток.
        Квадратная матрица нечетных размеров, где единицы обозначают клетки,
        учитываемые при расчете соседства, а нули - не учитываемые.

    Возвращает
    ----------
    np.ndarray
        Поле после выполнения всех итераций клеточного автомата.
    '''

    for _ in range(num_iterations):
        grid = UpdateField(grid, live_cell_value, dead_cell_value, neighborhood_kernel)

    return grid
