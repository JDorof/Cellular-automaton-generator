import gradients

'''Image'''
height = 150
width = 150


'''Colors'''
counter = 10
chances = [1, 10]
gradient = gradients.black_orange_yellow_white
# gradient = gradients.ocean_beach_forest
# gradient = gradients.black_to_white

'''Neighborhoods'''
standart3x3 = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 0], [0, 1], [1, -1], [1, 0], [1, 1]]
moore_neighborhood_1order = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

moore_neighborhood_2order = [[-2, -2], [-2, -1], [-2, 0], [-2, 1], [-2, 2],
                             [-1, -2], [-1, -1], [-1, 0], [-1, 1], [-1, 2],
                             [0, -2], [0, -1], [0, 1], [0, 2],
                             [1, -2], [1, -1], [1, 0], [1, 1], [1, 2],
                             [2, -2], [2, -1], [2, 0], [2, 1], [2, 2]]

plus = [[-1, 0], [0, -1], [0, 1], [1, 0]]
cross = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
horizontal = [[0, -1], [0, 1]]
vertical = [[-1, 0], [1, 0]]

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

