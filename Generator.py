import rules

import numpy as np
from random import randint

# field = np.array([rules.chances[randint(0, len(rules.chances) - 1)] for x in range(rules.height * rules.width)]).reshape(rules.width, rules.height)

def Shuffle_field(field, cell_type: list, field_type: list, chance: int):
    for y in range(rules.height):
        for x in range(rules.width):
            if field[y][x] in field_type and randint(1, 10) <= chance:
                field[y][x] = cell_type[randint(0, len(cell_type) - 1)]
    return field

def NarrowingTheField(new_field):
    field = np.zeros((rules.height, rules.width), dtype="int32")
    for y in range(rules.height):
        for x in range(rules.width):
            field[y][x] = new_field[y + 1][x + 1]
    return field


def FieldExpansion(field):
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
    new_field[rules.height + 1][rules.width + 1] = field[rules.height - 1][rules.width - 1]
    return new_field

def Blur(field):
    
    

def Neighborhood(field, x0: int, y0: int, cell_type: int, neighborhood_type):

    '''Число соседей определенного типа (cell_type) в окрестности (neighborhood_type) у заданной клетки'''

    counter = 0
    for y, x in neighborhood_type:
        x += x0
        y += y0
        if x < 0 or x >= rules.width or y < 0 or y >= rules.height: continue
        if field[y][x] == cell_type:
                counter += 1
    return counter

def Generate(field, cell_type: int, field_type: int, iterations: int, neighborhood_type):

    new_field = field.copy()

    for i in range(iterations):
        for y in range(rules.height):
            for x in range(rules.width):

                # pass

# Рабочий вариант, но костыль, который будет неправильно работать не в "День и ночь"

                if Neighborhood(field, x, y, cell_type, neighborhood_type) in rules.Birth[cell_type]:
                        new_field[y][x] = cell_type
                elif field[y][x] == cell_type:
                    if Neighborhood(field, x, y, field_type, neighborhood_type) in rules.Birth[cell_type]:
                        new_field[y][x] = field_type

# Полурабочий вариант, так как выдает много меньше нужного cell_type клеток

                # if field[y][x] ==  field_type:
                #     if Neighborhood(field, x, y, cell_type, neighborhood_type) in rules.Birth[cell_type]:
                #         new_field[y][x] = cell_type
                #     else:
                #         new_field[y][x] = field_type
                # elif field[y][x] == cell_type:
                #     if Neighborhood(field, x, y, cell_type, neighborhood_type) in rules.Survive[cell_type]:
                #         new_field[y][x] = cell_type
                #     else:
                #         new_field[y][x] = field_type

        field = new_field.copy()

    return field
                    
                
                    





# field = np.array([number_list[randint(0, len(number_list) - 1)] for x in range(height * width)]).reshape(width, height)
