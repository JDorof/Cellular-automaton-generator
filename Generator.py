import rules

import numpy as np
from random import randint

field = np.array([rules.chances[randint(0, len(rules.chances) - 1)] for x in range(rules.height * rules.width)]).reshape(rules.width, rules.height)

def Neighborhood(x0, y0, cell_type, neighborhood_type):

    '''Число соседей определенного типа (cell_type) в окрестности (neighborhood_type) у заданной клетки'''

    counter = 0
    for y, x in neighborhood_type:
        x += x0
        y += y0
        if x < 0 or x >= rules.width or y < 0 or y >= rules.height: continue
        if field[y][x] == cell_type:
                counter += 1
    return counter

def Generate():

    global  field

    new_field = field.copy()

    for i in range(rules.iteratons):
        for y in range(rules.height):
            for x in range(rules.width):
                match field[y][x]:
                    case 0:
                        if Neighborhood(x, y, 9, rules.moore_neighborhood) in rules.Birth[9]:
                            new_field[y][x] = 9
                    case 9:
                        if Neighborhood(x, y, 9, rules.moore_neighborhood) not in rules.Survive[9]:
                            new_field[y][x] = 0
        field = new_field.copy()

    return field
                    
                
                    





# field = np.array([number_list[randint(0, len(number_list) - 1)] for x in range(height * width)]).reshape(width, height)
