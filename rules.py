import gradients
import numpy as np
import time

'''seed'''
seed = str(time.time())
# seed = "aboab"

'''Image'''
'''
boundary:
    Правило, указывающее на способ обработки границы:
        fill - дополняет входные массивы значением заполнения. (по умолчанию)
        wrap - круговые граничные условия.
        symm - симметричные граничные условия.
'''
height = 200
width = 200
boundary = "wrap"
# boundary = "fill"
# boundary = "symm"

'''Colors'''
gradient = gradients.black_orange_yellow_white
# gradient = [x for x in reversed(gradients.ocean_beach_forest)]


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

