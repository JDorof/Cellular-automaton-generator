import numpy as np
import scipy.signal
import time
import random
from PIL import Image


class SeedClass:
    seed = str(time.time())
    random.seed(a=seed, version=2)
    np.random.seed(seed=random.randint(0, 2^32 - 1))

    @staticmethod
    def ChangeSeed(new_seed: str):
        SeedClass.seed = new_seed
        random.seed(a=new_seed, version=2)
        np.random.seed(seed=random.randint(0, 2^32 - 1))


class NeighborhoodClass:

    standart3x3 = np.ones((3, 3), dtype=int)
    '''
    1 1 1\n
    1 1 1\n
    1 1 1
    '''

    moore_neighborhood_1order = np.ones((3, 3), dtype=int)
    '''
    1 1 1\n
    1 0 1\n
    1 1 1
    '''
    moore_neighborhood_1order[1, 1] = 0

    moore_neighborhood_2order = np.ones((5, 5), dtype=int)
    '''
    1 1 1 1 1\n
    1 1 1 1 1\n
    1 1 0 1 1\n
    1 1 1 1 1\n
    1 1 1 1 1
    '''
    moore_neighborhood_2order[2, 2] = 0

    plus = np.ones((3, 3), dtype=int)
    '''
    0 1 0\n
    1 1 1\n
    0 1 0
    '''
    plus[0][0] = plus[0][2] = plus[2][0] = plus[2][2] = 0

    cross = np.ones((3, 3), dtype=int)
    '''
    1 0 1\n
    0 1 0\n
    1 0 1
    '''
    cross[0][1] = cross[1][0] = cross[1][2] = cross[2][1] = 0

    horizontal = np.zeros((3, 3), dtype=int)
    '''
    0 0 0\n
    1 1 1\n
    0 0 0
    '''
    horizontal[1][0] = horizontal[1][2] = horizontal[1][1] = 1

    vertical = np.zeros((3, 3), dtype=int)
    '''
    0 1 0\n
    0 1 0\n
    0 1 0
    '''
    vertical[0][1] = vertical[2][1] = vertical[1][1] = 1


class BlurClass:

    # сумма всех элементов должа быть равна 1
    # размер матрицы оставляем 3 на 3, так как в функции Blur при вычислении используется поле 3 на 3

    standart3x3 = np.array([
        [0.0625, 0.125, 0.0625],
        [0.125, 0.25, 0.125],
        [0.0625, 0.125, 0.0625]
    ])
    '''
    [[0.0625, 0.125, 0.0625],\n
    [0.125, 0.25, 0.125],\n
    [0.0625, 0.125, 0.0625]]
    '''

    standart5x5 = np.array([
        [0.00296902, 0.01330621, 0.02193823, 0.01330621, 0.00296902],
        [0.01330621, 0.0596343,  0.09832033, 0.0596343,  0.01330621],
        [0.02193823, 0.09832033, 0.16210282, 0.09832033, 0.02193823],
        [0.01330621, 0.0596343,  0.09832033, 0.0596343,  0.01330621],
        [0.00296902, 0.01330621, 0.02193823, 0.01330621, 0.00296902]
    ])
    '''
    [[0.00296902, 0.01330621, 0.02193823, 0.01330621, 0.00296902],\n
    [0.01330621, 0.0596343,  0.09832033, 0.0596343,  0.01330621],\n
    [0.02193823, 0.09832033, 0.16210282, 0.09832033, 0.02193823],\n
    [0.01330621, 0.0596343,  0.09832033, 0.0596343,  0.01330621],\n
    [0.00296902, 0.01330621, 0.02193823, 0.01330621, 0.00296902]]
    '''

    outside = np.array([
        [0.125, 0.125, 0.125],
        [0.125, 0.0, 0.125],
        [0.125, 0.125, 0.125]
    ])
    '''
    [[0.125, 0.125, 0.125],\n
    [0.125, 0.0, 0.125],\n
    [0.125, 0.125, 0.125]]
    '''

    square = np.array([
        [0.111111, 0.111111, 0.111111],
        [0.111111, 0.111111, 0.111111],
        [0.111111, 0.111111, 0.111111]
    ])
    '''
    [[0.111111, 0.111111, 0.111111],\n
    [0.111111, 0.111111, 0.111111],\n
    [0.111111, 0.111111, 0.111111]]
    '''

    cross = np.array([
        [0.15, 0.0, 0.15],
        [0.0, 0.4, 0.0],
        [0.15, 0.0, 0.15]
    ])
    '''
    [[0.15, 0.0, 0.15],\n
    [0.0, 0.4, 0.0],\n
    [0.15, 0.0, 0.15]]
    '''

    plus = np.array([
        [0.0, 0.15, 0.0],
        [0.15, 0.4, 0.15],
        [0.0, 0.15, 0.0]
    ])
    '''
    [[0.0, 0.15, 0.0],\n
    [0.15, 0.4, 0.15],\n
    [0.0, 0.15, 0.0]]
    '''


    outside_standart = np.array([
        [0.083333, 0.166666, 0.083333],
        [0.166666, 0.0, 0.166666],
        [0.083333, 0.166666, 0.083333]
    ])
    '''
    [[0.083333, 0.166666, 0.083333],\n
    [0.166666, 0.0, 0.166666],\n
    [0.083333, 0.166666, 0.083333]]
    '''

    outside_cross = np.array([
        [0.25, 0.0, 0.25],
        [0.0, 0.0, 0.0],
        [0.25, 0.0, 0.25]
    ])
    '''
    [[0.25, 0.0, 0.25],\n
    [0.0, 0.0, 0.0],\n
    [0.25, 0.0, 0.25]]
    '''

    outside_plus = np.array([
        [0.0, 0.25, 0.0],
        [0.25, 0.0, 0.25],
        [0.0, 0.25, 0.0]
    ])
    '''
    [[0.0, 0.25, 0.0],\n
    [0.25, 0.0, 0.25],\n
    [0.0, 0.25, 0.0]]
    '''

    horizontal = np.array([
        [0.0, 0.0, 0.0],
        [0.25, 0.5, 0.25],
        [0.0, 0.0, 0.0]
    ])
    '''
    [[0.0, 0.0, 0.0],\n
    [0.25, 0.5, 0.25],\n
    [0.0, 0.0, 0.0]]
    '''

    vertical = np.array([
        [0.0, 0.25, 0.0],
        [0.0, 0.5, 0.0],
        [0.0, 0.25, 0.0]
    ])
    '''
    [[0.0, 0.25, 0.0],\n
    [0.0, 0.5, 0.0],\n
    [0.0, 0.25, 0.0]]
    '''

    horizontal_cross = np.array([
        [0.1, 0.0, 0.1],
        [0.15, 0.3, 0.15],
        [0.1, 0.0, 0.1]
    ])
    '''
    [[0.1, 0.0, 0.1],\n
    [0.15, 0.3, 0.15],\n
    [0.1, 0.0, 0.1]]
    '''

    vertical_cross = np.array([
        [0.1, 0.15, 0.1],
        [0.0, 0.3, 0.0],
        [0.1, 0.15, 0.1]
    ])
    '''
    [[0.1, 0.15, 0.1],\n
    [0.0, 0.3, 0.0],\n
    [0.1, 0.15, 0.1]]
    '''

    down = np.array([
        [0.15, 0.2, 0.15],
        [0.0, 0.4, 0.0],
        [0.0, 0.0, 0.0]
    ])
    '''
    [[0.15, 0.2, 0.15],\n
    [0.0, 0.4, 0.0],\n
    [0.0, 0.0, 0.0]]
    '''

    # contrast = np.array([
    #     [-1.0, -1.0, -1.0],
    #     [-1.0, 9.0, -1.0],
    #     [-1.0, -1.0, -1.0]
    # ])


class GradientClass:


    black_to_white = [(0, 0, 0), (28, 28, 28), (56, 56, 56), (85, 85, 85), (113, 113, 113), (141, 141, 141), (170, 170, 170), (198, 198, 198), (226, 226, 226), (255, 255, 255)]
    ocean_beach_forest = [(5, 6, 27), (11, 15, 134), (25, 68, 178), (60, 143, 215), (60, 208, 215), (237, 255, 68), (79, 255, 0), (70, 200, 11), (29, 145, 32), (9, 110, 12)]
    black_orange_yellow_white = [(0, 0, 0, 255), (63, 27, 0, 255), (127, 54, 0, 255), (191, 81, 0, 255), (255, 108, 0, 255), (255, 157, 0, 255), (255, 206, 0, 255), (255, 255, 0, 255), (255, 255, 127, 255), (255, 255, 255, 255)]
    dark_grey_brown = [(42, 39, 30), (48, 46, 39), (55, 53, 48), (67, 65, 59), (79, 77, 71), (91, 89, 83), (103, 101, 95), (116, 113, 107), (91, 89, 83), (55, 53, 48)]
    grass = [(21, 21, 21), (23, 27, 24), (26, 33, 27), (28, 40, 31), (31, 46, 34), (34, 53, 38), (42, 69, 47), (50, 85, 57), (59, 102, 67), (69, 119, 77)]

    all_gradients = [black_to_white, ocean_beach_forest, black_orange_yellow_white, dark_grey_brown, grass]

    def ReadGradient(path):
        to_read = Image.open(path)
        gradient = [to_read.getpixel((x, 0)) for x in range(0, 10)]
        return gradient


    def SaveGradient(gradient, name):
        to_save = Image.new('RGBA', (10, 1))
        to_save.putdata(gradient)
        to_save.save(f'gradients/{name}')


def InitializeField(chances, shape):
    return np.random.choice(chances, size=shape).astype("int32")


def ReplaceCells(
        field: np.ndarray
        , replace: list
        , to: list
        , p: float = 1
        ) -> np.ndarray:

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


def Blur(
        field: np.ndarray
        , blur_type: np.ndarray
        , target_values: set = set(range(1, 11))
        , iterations: int = 1
        , boundary="wrap"
        ) -> np.ndarray:
    
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

    for _ in range(iterations):
        # Создаем маску для клеток, которые нужно размыть
        blur_mask = np.isin(field, list(target_values))

        # Применяем размытие ко всему полю
        blurred_field = scipy.signal.convolve2d(field, blur_type, mode='same', boundary=boundary)

        # Восстанавливаем оригинальные значения на местах, которые не подлежат размытию
        blurred_field[~blur_mask] = field[~blur_mask]

        # Округляем значения и приводим их к целым числам
        field = np.round(blurred_field).astype(dtype="int32")

    return np.round(field).astype(dtype="int32")


def UpdateField(
                grid: np.ndarray
                , live_cell_value: int
                , dead_cell_value: int
                , birth_rule: list
                , survive_rule: list
                , neighborhood_kernel: np.ndarray
                , boundary
                ) -> np.ndarray:
    
    '''
    Обновляет состояние клеток в поле по заданным правилам.

    Параметры
    ----------
    grid: np.ndarray
        Исходное поле, представляющее собой матрицу чисел.
    live_cell_value: int
        Значение, обозначающее "живую" клетку.
    dead_cell_value: int
        Значение, обозначающее "мертвую" клетку.
    birth_rule: list
        Множество, в котором хранится кол-во соседей,
        при которых "мертвая" клетка "оживает".
    survive_rule: list
        Множество, в котором хранится кол-во соседей,
        при которых "живая" клетка остается "живой".
    neighborhood_kernel: np.ndarray
        Ядро свертки, определяющее соседство клеток.
        Квадратная матрица нечетных размеров, где единицы обозначают клетки,
        учитываемые при расчете соседства, а нули - не учитываемые.
    boundary:
    Правило, указывающее на способ обработки границы:
        fill - дополняет входные массивы значением заполнения. (по умолчанию)
        wrap - круговые граничные условия.
        symm - симметричные граничные условия.

    Возвращает
    ----------
    - np.ndarray - Обновленное поле.
    '''

    # Создаем маску для клеток, которые считаются "живыми"
    live_cell_mask = (grid == live_cell_value)

    # Применяем ядро свертки для подсчета соседей
    neighbor_counts = scipy.signal.convolve2d(live_cell_mask, neighborhood_kernel, mode='same', boundary=boundary)

    # Определяем маски для клеток, которые должны "родиться" и "выжить"
    birth_mask = (grid == dead_cell_value) & np.isin(neighbor_counts, birth_rule)
    survival_mask = (grid == live_cell_value) & np.isin(neighbor_counts, survive_rule)

    # Создаем копию поля для обновления
    updated_grid = grid.copy()

    # Обновляем состояния клеток
    updated_grid[birth_mask] = live_cell_value
    updated_grid[~survival_mask & live_cell_mask] = dead_cell_value

    return updated_grid


def RunAutomaton(
                grid: np.ndarray
                , live_cell_value: int
                , dead_cell_value: int
                , birth_rule: list
                , survive_rule: list
                , num_iterations: int
                , neighborhood_kernel: np.ndarray
                , boundary="wrap"
                ) -> np.ndarray:
    
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
    birth_rule: list
        Множество, в котором хранится кол-во соседей,
        при которых "мертвая" клетка "оживает".
    survive_rule: list
        Множество, в котором хранится кол-во соседей,
        при которых "живая" клетка остается "живой".
    num_iterations: int
        Количество итераций для выполнения клеточного автомата.
    neighborhood_kernel: np.ndarray
        Ядро свертки, определяющее соседство клеток.
        Квадратная матрица нечетных размеров, где единицы обозначают клетки,
        учитываемые при расчете соседства, а нули - не учитываемые.
    boundary:
    Правило, указывающее на способ обработки границы:\n
        fill - дополняет входные массивы значением заполнения. (по умолчанию)\n
        wrap - круговые граничные условия.\n
        symm - симметричные граничные условия.

    Возвращает
    ----------
    np.ndarray
        Поле после выполнения всех итераций клеточного автомата.
    '''

    for _ in range(num_iterations):
        grid = UpdateField(grid, live_cell_value, dead_cell_value, birth_rule, survive_rule, neighborhood_kernel, boundary=boundary)

    return grid


'''SaveLoad Functions'''


def SaveImage(field: np.ndarray, path: str, gradient: list):
    sizes = field.shape
    im = Image.new('RGB', sizes)
    result = list(field.reshape(sizes[0] * sizes[1]))
    try:
        for i in range(sizes[0] * sizes[1]):
            result[i] = gradient[result[i] - 1]
    except IndexError:
        print("SaveImage function:")
        print(f"ERROR: You have int values bigger than 'max index - 1': {result[i] - 1}")
        exit()
    im.putdata(result)
    im.save(path)


def SaveMatrix(field: np.ndarray, path):
    np.savetxt(path, field, delimiter=' ', fmt='%d')


def LoadMatrix(path):
    return np.loadtxt(path, dtype="int32")


def SaveCode(name_of_file, path):

    file = open(name_of_file)

    with open(path, mode="w") as save:
        for line in file:
            li=line.strip()
            if not li.startswith("#"):
                save.write(line)
        save.write(f'\n# Generator.{SeedClass.seed = }')


def AverageAmountOfFields(*fields):
    field = np.round(sum(fields) / len(fields)).astype(dtype="int32")
    return field
