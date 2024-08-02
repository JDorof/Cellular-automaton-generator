'''Переписать правила в виде B3/S23, где B - birth, S - survive''' # TODO

import values

def AliveInMooreNeighborhood(x0, y0, field, width, heigth, cell_type):

    '''Число такого же типа (cell_type) соседей в окрестности Мура у заданной клетки'''

    counter = 0
    for y in range(y0 - 1, y0 + 2):
        for x in range(x0 - 1, x0 + 2):
            if x0 == x and y0 == y: continue
            if x < 0 or x >= width or y < 0 or y >= heigth: continue
            if field[y][x] == cell_type:
                counter += 1
    return counter


def GameLife(x, y, field, new_field, width, heigth, cell_type):

    '''Правило <<Игра жизнь>>. B3/S32'''

    if AliveInMooreNeighborhood(x, y, field, width, heigth, cell_type) == 3:
        new_field[y][x] = cell_type
    elif AliveInMooreNeighborhood(x, y, field, width, heigth, cell_type) == 2 and field[y][x] == 1:
        new_field[y][x] == cell_type
    else:
        new_field[y][x] = 0


def DayAndNight(x, y, field, new_field, width, heigth, cell_type):
    
    '''Правило <<День и ночь>>. B3678/S34678'''

    if AliveInMooreNeighborhood(x, y, field, width, heigth, cell_type) in [3, 6, 7, 8]:
        new_field[y][x] = cell_type
    elif AliveInMooreNeighborhood(x, y, field, width, heigth, cell_type) in [3, 4, 6, 7, 8] and field[y][x] == cell_type:
        new_field[y][x] = cell_type
    else:
        new_field[y][x] = 0
