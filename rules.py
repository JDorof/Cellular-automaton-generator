import gradients

'''Image'''
height = 200
width = 200

'''Colors'''
counter = 10
chances = [0, 9]
gradient = gradients.ocean_beach_forest

'''Neighborhoods'''
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
    9 : [3, 6, 7, 8], # day and night
    8 : [3, 6, 7, 8], # day and night
    0 : [3, 6, 7, 8] # day and night
}
Survive = {
    9 : [3, 4, 6, 7, 8], # day and night
    8 : [3, 4, 6, 7, 8], # day and night
    0 : [3, 4, 6, 7, 8] # day and night
}

# '''Generation'''
# iteratons = 250
