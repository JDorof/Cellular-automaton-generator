import random
import time

# Файл генератора без использования сторонних библиотек
# Немного обрезанный (все границы будут обрабатываться как wrap)

class SeedClass:

    seed = str(time.time())
    random.seed(a=seed, version=2)
    # np.random.seed(seed=random.randint(0, 2^32 - 1))

    @staticmethod
    def ChangeSeed(new_seed: str):
        SeedClass.seed = new_seed
        random.seed(a=new_seed, version=2)
        # np.random.seed(seed=random.randint(0, 2^32 - 1))


class NeighborhoodClass:
    '''
    Класс, в котором храняться ядра свертки, определяющее соседство клеток.
    Квадратная матрица нечетных размеров, где единицы обозначают клетки,
    учитываемые при расчете соседства, а нули - не учитываемые.
    '''


    standart3x3 = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    '''
    1 1 1\n
    1 1 1\n
    1 1 1
    '''

    moore_neighborhood_1order = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    '''
    1 1 1\n
    1 0 1\n
    1 1 1
    '''

    moore_neighborhood_2order = [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1]
    ]
    '''
    1 1 1 1 1\n
    1 1 1 1 1\n
    1 1 0 1 1\n
    1 1 1 1 1\n
    1 1 1 1 1
    '''

    plus = [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ]
    '''
    0 1 0\n
    1 1 1\n
    0 1 0
    '''

    cross = [
        [1, 0, 1],
        [0, 1, 0],
        [1, 0, 1]
    ]
    '''
    1 0 1\n
    0 1 0\n
    1 0 1
    '''

    horizontal_1order = [
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 0]
    ]
    '''
    0 0 0\n
    1 1 1\n
    0 0 0
    '''

    vertical_1order = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0]
    ]
    '''
    0 1 0\n
    0 1 0\n
    0 1 0
    '''

    horizontal_2order = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    '''
    0 0 0 0 0\n
    0 0 0 0 0\n
    1 1 1 1 1\n
    0 0 0 0 0\n
    0 0 0 0 0
    '''

    vertical_2order = [
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
    ]
    '''
    0 0 1 0 0\n
    0 0 1 0 0\n
    0 0 1 0 0\n
    0 0 1 0 0\n
    0 0 1 0 0
    '''


class BlurClass:
    '''
    Класс, в котором храняться ядра свертки для размытия.
    '''

    # сумма всех элементов должа быть равна 1

    standart3x3 = [
        [0.0625, 0.125, 0.0625],
        [0.125, 0.25, 0.125],
        [0.0625, 0.125, 0.0625]
    ]
    '''
    [[0.0625, 0.125, 0.0625],\n
    [0.125, 0.25, 0.125],\n
    [0.0625, 0.125, 0.0625]]
    '''

    standart5x5 = [
        [0.00296902, 0.01330621, 0.02193823, 0.01330621, 0.00296902],
        [0.01330621, 0.0596343,  0.09832033, 0.0596343,  0.01330621],
        [0.02193823, 0.09832033, 0.16210282, 0.09832033, 0.02193823],
        [0.01330621, 0.0596343,  0.09832033, 0.0596343,  0.01330621],
        [0.00296902, 0.01330621, 0.02193823, 0.01330621, 0.00296902]
    ]
    '''
    [[0.00296902, 0.01330621, 0.02193823, 0.01330621, 0.00296902],\n
    [0.01330621, 0.0596343,  0.09832033, 0.0596343,  0.01330621],\n
    [0.02193823, 0.09832033, 0.16210282, 0.09832033, 0.02193823],\n
    [0.01330621, 0.0596343,  0.09832033, 0.0596343,  0.01330621],\n
    [0.00296902, 0.01330621, 0.02193823, 0.01330621, 0.00296902]]
    '''

    outside = [
        [0.125, 0.125, 0.125],
        [0.125, 0.0, 0.125],
        [0.125, 0.125, 0.125]
    ]
    '''
    [[0.125, 0.125, 0.125],\n
    [0.125, 0.0, 0.125],\n
    [0.125, 0.125, 0.125]]
    '''

    square = [
        [0.111111, 0.111111, 0.111111],
        [0.111111, 0.111111, 0.111111],
        [0.111111, 0.111111, 0.111111]
    ]
    '''
    [[0.111111, 0.111111, 0.111111],\n
    [0.111111, 0.111111, 0.111111],\n
    [0.111111, 0.111111, 0.111111]]
    '''

    cross = [
        [0.15, 0.0, 0.15],
        [0.0, 0.4, 0.0],
        [0.15, 0.0, 0.15]
    ]
    '''
    [[0.15, 0.0, 0.15],\n
    [0.0, 0.4, 0.0],\n
    [0.15, 0.0, 0.15]]
    '''

    plus = [
        [0.0, 0.15, 0.0],
        [0.15, 0.4, 0.15],
        [0.0, 0.15, 0.0]
    ]
    '''
    [[0.0, 0.15, 0.0],\n
    [0.15, 0.4, 0.15],\n
    [0.0, 0.15, 0.0]]
    '''


    outside_standart = [
        [0.083333, 0.166666, 0.083333],
        [0.166666, 0.0, 0.166666],
        [0.083333, 0.166666, 0.083333]
    ]
    '''
    [[0.083333, 0.166666, 0.083333],\n
    [0.166666, 0.0, 0.166666],\n
    [0.083333, 0.166666, 0.083333]]
    '''

    outside_cross = [
        [0.25, 0.0, 0.25],
        [0.0, 0.0, 0.0],
        [0.25, 0.0, 0.25]
    ]
    '''
    [[0.25, 0.0, 0.25],\n
    [0.0, 0.0, 0.0],\n
    [0.25, 0.0, 0.25]]
    '''

    outside_plus = [
        [0.0, 0.25, 0.0],
        [0.25, 0.0, 0.25],
        [0.0, 0.25, 0.0]
    ]
    '''
    [[0.0, 0.25, 0.0],\n
    [0.25, 0.0, 0.25],\n
    [0.0, 0.25, 0.0]]
    '''

    horizontal = [
        [0.0, 0.0, 0.0],
        [0.25, 0.5, 0.25],
        [0.0, 0.0, 0.0]
    ]
    '''
    [[0.0, 0.0, 0.0],\n
    [0.25, 0.5, 0.25],\n
    [0.0, 0.0, 0.0]]
    '''

    vertical = [
        [0.0, 0.25, 0.0],
        [0.0, 0.5, 0.0],
        [0.0, 0.25, 0.0]
    ]
    '''
    [[0.0, 0.25, 0.0],\n
    [0.0, 0.5, 0.0],\n
    [0.0, 0.25, 0.0]]
    '''

    horizontal_cross = [
        [0.1, 0.0, 0.1],
        [0.15, 0.3, 0.15],
        [0.1, 0.0, 0.1]
    ]
    '''
    [[0.1, 0.0, 0.1],\n
    [0.15, 0.3, 0.15],\n
    [0.1, 0.0, 0.1]]
    '''

    vertical_cross = [
        [0.1, 0.15, 0.1],
        [0.0, 0.3, 0.0],
        [0.1, 0.15, 0.1]
    ]
    '''
    [[0.1, 0.15, 0.1],\n
    [0.0, 0.3, 0.0],\n
    [0.1, 0.15, 0.1]]
    '''

    down = [
        [0.15, 0.2, 0.15],
        [0.0, 0.4, 0.0],
        [0.0, 0.0, 0.0]
    ]
    '''
    [[0.15, 0.2, 0.15],\n
    [0.0, 0.4, 0.0],\n
    [0.0, 0.0, 0.0]]
    '''


class GradientClass:
#     '''
#     Класс, в котором хранятся разные градиенты
#     и функции чтения и записи этих градиентов
#     '''


#     black_to_white = [(0, 0, 0), (28, 28, 28), (56, 56, 56), (85, 85, 85), (113, 113, 113), (141, 141, 141), (170, 170, 170), (198, 198, 198), (226, 226, 226), (255, 255, 255)]
#     ocean_beach_forest = [(5, 6, 27), (11, 15, 134), (25, 68, 178), (60, 143, 215), (60, 208, 215), (237, 255, 68), (79, 255, 0), (70, 200, 11), (29, 145, 32), (9, 110, 12)]
#     black_orange_yellow_white = [(0, 0, 0, 255), (63, 27, 0, 255), (127, 54, 0, 255), (191, 81, 0, 255), (255, 108, 0, 255), (255, 157, 0, 255), (255, 206, 0, 255), (255, 255, 0, 255), (255, 255, 127, 255), (255, 255, 255, 255)]
#     dark_grey_brown = [(42, 39, 30), (48, 46, 39), (55, 53, 48), (67, 65, 59), (79, 77, 71), (91, 89, 83), (103, 101, 95), (116, 113, 107), (91, 89, 83), (55, 53, 48)]
#     grass = [(21, 21, 21), (23, 27, 24), (26, 33, 27), (28, 40, 31), (31, 46, 34), (34, 53, 38), (42, 69, 47), (50, 85, 57), (59, 102, 67), (69, 119, 77)]

#     all_gradients = [black_to_white, ocean_beach_forest, black_orange_yellow_white, dark_grey_brown, grass]

#     def ReadGradient(path: str):
#         '''
#         Функция чтения градиента из файла
#         ---
#         Параметры:\n
#         - path: str - путь до файла.
#         ---
#         Возвращает:\n
#         - list - Массив с цветами градиента.\n
#         '''

#         to_read = Image.open(path)
#         gradient = [to_read.getpixel((x, 0)) for x in range(0, 10)]
#         return gradient


#     def SaveGradient(gradient: list, path: str):
#         '''
#         Функция сохранения градиента в файл\n
#         ---
#         Параметры:\n
#         - gradient: list - Массив с цветами градиента.\n
#         - path: str - путь до файла.
#         '''

#         to_save = Image.new('RGBA', (10, 1))
#         to_save.putdata(gradient)
#         to_save.save(path)
    pass


def InitializeField(chances: list, shape: tuple) -> list:
    '''
    Функция случайного заполнения клеток числами из chances в матрицу с размерами shape.
    ---
    Параметры:\n
    - chances: list - Массив с значениями, из которых потом будет случайным образом наполнятся клетки матрицы.\n
    - shape: tuple - размеры матрицы.
    ---
    Возвращает:\n
    - np.ndarray - Матрица со случайными значениями.\n
    '''
    field = []

    for y in range(shape[1]):
        field.append([])
        for x in range(shape[0]):
            field[y].append(chances[random.randint(0, len(chances) - 1)])

    return field


def ReplaceCells(
        field: list
        , replace: list
        , to: list
        , p: float = 1.0
        , mask: list = None
        ) -> list:

    '''
    Функция случайной замены клеток типов из target_types на типы из replacement_types с заданной вероятностью.
    ---
    Параметры:\n
    - field: list - Массив, в котором производится замена клеток.\n
    - replace: list - Список типов клеток, которые нужно заменить.\n
    - to: list - Список типов клеток, на которые будут заменены целевые клетки.\n
    - p: float - Вероятность замены клеток, значение от 0 до 1.
    - mask: list - Маска, где будут происходить замены (1 - True, 0 - False). 
    ---
    Возвращает:\n
    - list - Матрица с замененными клетками.\n
    '''

    field_height = len(field)
    field_width = len(field[0])

    # Создаем маску из 1, если она изначально не задана
    if mask is None:
        mask = []
        for y in range(field_height):
            mask.append([])
            for x in range(field_width):
                mask[y].append(1)
        
    field_after = []        
    for y in range(field_height):
        field_after.append([])
        field_after[y] = field[y].copy()
        for x in range(field_width):
            if not (mask[y][x] and field[y][x] in replace):
                continue
                # mask[y][x] = 0
            if random.random() <= p:
                field_after[y][x] = to[random.randint(0, len(to) - 1)]

    return field_after


def Blur(
        field: list
        , blur_type: list
        , target_values: list = list(range(1, 11))
        , iterations: int = 1
        ) -> list:
    
    '''
    Функция для размытия числового массива с сохранением значений, не входящих в список target_values.
    ---
    Параметры:\n
    - field: list - Матрица, которую нужно размыть.\n
    - blur_type: list - Ядро свертки для размытия.\n
    - target_values: list - Список значений, которые должны быть размыты. Значения, не входящие в этот список, остаются неизменными.\n
    - iterations: int - Количество итераций размытия.\n
    - boundary:\n
    Правило, указывающее на способ обработки границы:\n
    - fill - Значения за пределами массива считаются равными фиксированному значению, указанному параметром fillvalue (по умолчанию это 0).\n
    - wrap - Циклическое продолжение, при котором границы соединяются, как будто массив закольцован.\n
    - symm - Значения за пределами массива симметрично отражаются от границ массива.
    ---
    Возвращает:\n
    - list - Матрица после размытия.
    '''

    blur_height = len(blur_type)
    blur_width = len(blur_type[0])

    field_copy = []
    next_field = []
    field_height = len(field) 
    field_width = len(field[0])

    for y in range(field_height):
        field_copy.append(field[y].copy())
    
    for _ in range(iterations):
        for y in range(field_width):
            # Создаем копию поля для вычислений
            next_field.append(field[y].copy())
            for x in range(field_width):
                convolve = 0
                if field_copy[y][x] not in target_values:
                    continue
                for ky in range(-(blur_height//2), (blur_height//2) + 1):
                    for kx in range(-(blur_width//2), (blur_width//2) + 1):
                        ny = (y + ky) % field_height  # Закольцованная координата по вертикали
                        nx = (x + kx) % field_width  # Закольцованная координата по горизонтали
                        convolve += blur_type[ky + blur_height//2][kx + blur_width//2] * field_copy[ny][nx]
                next_field[y][x] = round(convolve)
        # Обновление текущего состояния поля
        field_copy = []
        for y in range(field_width):
            field_copy.append(next_field[y].copy())

    return field_copy


def MedianFilter(
        field: list
        , kernel_size: int
        , target_values: set = set(range(1, 11))
        , iterations: int = 1
        , boundary: str = "wrap"
        , cval: int = 0
        ) -> list:
    
    '''
    Функция, примняющая медианный фильтр к матрице с сохранением значений, не входящих в список target_values.
    ---
    Параметры:\n
    - field: list - Матрица, которую нужно размыть.\n
    - kernel_size: int - Размер фильтра.\n
    - target_values: list - Список значений, которые должны быть размыты. Значения, не входящие в этот список, остаются неизменными.\n
    - iterations: int - Количество итераций размытия.\n
    - boundary:\n
    Правило, указывающее на способ обработки границы:\n
    - reflect - Значения на границах повторяются в зеркальном отображении.\n
    - constant - За пределами массива используется фиксированное значение, определяемое параметром cval (по умолчанию 0).\n
    - nearest - Используются ближайшие значения к границе.\n
    - mirror - Похож на reflect, но с небольшим отличием: границы повторяются так, как будто массив зеркально отображается без повторения самого края.\n
    - wrap - Циклическое продолжение, при котором границы соединяются, как будто массив закольцован.
    ---
    Возвращает:\n
    - list - Матрица после размытия.
    '''
    
    field_copy = field.copy()

    # Создаем маску для клеток, которые будут заменены медианным фильтром
    median_mask = np.isin(field, list(target_values))
    
    for _ in range(iterations):
        
        # Применяем медианный фильтр
        medfilt_field = scipy.ndimage.median_filter(field_copy,size=kernel_size, mode=boundary, cval=cval)
        
        # Восстанавливаеем оригинальные значения на местах, которые не подлежат изменению фильтром
        medfilt_field[~median_mask] = field_copy[~median_mask]

        field_copy = medfilt_field.copy()
    
    return medfilt_field



def RunAutomaton(
                field: list,
                live_cell_value: int,
                dead_cell_value: int,
                birth_rule: list,
                survive_rule: list,
                num_iterations: int,
                neighborhood_kernel: list
                ) -> list:
    """
    Запускает процесс клеточного автомата для заданного количества итераций.

    Параметры:
    - field: list - Исходное поле, представляющее собой матрицу чисел.
    - live_cell_value: int - Значение, обозначающее "живую" клетку.
    - dead_cell_value: int - Значение, обозначающее "мертвую" клетку.
    - birth_rule: list - Кол-во соседей, при которых "мертвая" клетка "оживает".
    - survive_rule: list - Кол-во соседей, при которых "живая" клетка остается "живой".
    - num_iterations: int - Количество итераций для выполнения клеточного автомата.
    - neighborhood_kernel: list - Ядро соседства, квадратная матрица нечетного размера с 1 и 0.
    
    Возвращает:
    - list - Матрица после выполнения всех итераций клеточного автомата.
    """
    
    field_copy = []
    next_field = []
    field_height = len(field)
    field_width = len(field[0])
    kernel_size = len(neighborhood_kernel)
    kernel_radius = kernel_size // 2

    # копирование массивов (без этого будет ошибки)
    for y in range(field_height):
        field_copy.append(field[y].copy())

    # Выполнение указанного числа итераций
    for _ in range(num_iterations):
        for y in range(field_height):
            # Создаем копию поля для вычислений
            next_field.append(field[y].copy())
            for x in range(field_width):
                # Подсчет живых соседей
                live_neighbors = 0
                for ky in range(-kernel_radius, kernel_radius + 1):
                    for kx in range(-kernel_radius, kernel_radius + 1):
                        ny = (y + ky) % field_height  # Закольцованная координата по вертикали
                        nx = (x + kx) % field_width  # Закольцованная координата по горизонтали
                        if neighborhood_kernel[ky + kernel_radius][kx + kernel_radius] == 1:
                            if field_copy[ny][nx] == live_cell_value:
                                live_neighbors += 1

                # Применение правил рождения и выживания
                if field_copy[y][x] == live_cell_value:
                    # Проверка правила выживания
                    if live_neighbors not in survive_rule:
                        next_field[y][x] = dead_cell_value
                elif field_copy[y][x] == dead_cell_value:
                    # Проверка правила рождения
                    if live_neighbors in birth_rule:
                        next_field[y][x] = live_cell_value

        # Обновление текущего состояния поля
        field_copy = []
        for y in range(field_width):
            field_copy.append(next_field[y].copy())

    return field_copy


def AverageAmountOfFields(*fields) -> list:
    '''
    Функция, которая складвает все матрицы, после деля каждое значение на кол-во матриц.
    ---
    Параметры:\n
    - *fields - массив с матрицами
    ---
    Возвращает:\n
    - list - Итоговая матрица.
    '''
    field_result = []
    for y in range(len(fields[0])):
        field_result.append([])
        for x in range(len(fields[0][0])):
            field_result[y].append(0)
            for field in fields:
                field_result[y][x] += field[y][x]
            field_result[y][x] = round(field_result[y][x] / len(fields))


    return field_result
