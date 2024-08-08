import gradients
import numpy as np

'''Image'''
height = 100
width = 100


'''Colors'''
counter = 10
gradient = gradients.black_orange_yellow_white
# gradient = gradients.ocean_beach_forest
# gradient = gradients.forest_beach_ocean
# gradient = gradients.black_to_white
# gradient = gradients.white_to_black
chances = [1, 10]

'''Neighborhoods'''
standart3x3 = np.ones((3, 3), dtype=int)

moore_neighborhood_1order = np.ones((3, 3), dtype=int)
moore_neighborhood_1order[1, 1] = 0

moore_neighborhood_2order = np.ones((5, 5), dtype=int)
moore_neighborhood_2order[2, 2] = 0

plus = np.ones((3, 3), dtype=int)
plus[0][0] = plus[0][2] = plus[2][0] = plus[2][2] = 0

cross = np.ones((3, 3), dtype=int)
cross[0][1] = cross[1][0] = cross[1][2] = cross[2][1] = 0

# horizontal = [[0, -1], [0, 1]]
# vertical = [[-1, 0], [1, 0]]

'''Rules'''
Birth = {
    10 : [3, 6, 7, 8], # day and night for moore
    9 : [3, 6, 7, 8], # day and night for moore
    8 : [3, 6, 7, 8], # day and night for moore
    7 : [3, 6, 7, 8], # day and night for moore
    6 : [3, 6, 7, 8], # day and night for moore
    5 : [3, 6, 7, 8], # day and night for moore
    4 : [3, 6, 7, 8], # day and night for moore
    3 : [3, 6, 7, 8], # day and night for moore
    2 : [3, 6, 7, 8], # day and night for moore
    1 : [3, 6, 7, 8], # day and night for moore
}

Survive = {
    10 : [3, 4, 6, 7, 8], # day and night for moore
    9 : [3, 4, 6, 7, 8], # day and night for moore
    8 : [3, 4, 6, 7, 8], # day and night for moore
    7 : [3, 4, 6, 7, 8], # day and night for moore
    6 : [3, 4, 6, 7, 8], # day and night for moore
    5 : [3, 4, 6, 7, 8], # day and night for moore
    4 : [3, 4, 6, 7, 8], # day and night for moore
    3 : [3, 4, 6, 7, 8], # day and night for moore
    2 : [3, 4, 6, 7, 8], # day and night for moore
    1 : [3, 4, 6, 7, 8], # day and night for moore
}

