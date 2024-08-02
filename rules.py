import gradients

'''Image'''
height = 200
width = 200

'''Colors'''
counter = 10
chances = [0, 9]
gradient = gradients.white_to_black

'''Neighborhoods'''
moore_neighborhood = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
plus = [[-1, 0], [0, -1], [0, 1], [1, 0]]
cross = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
horizontal = [[0, -1], [0, 1]]
vertical = [[-1, 0], [1, 0]]

'''Rules'''
Birth = {
    9 : [3, 6, 7, 8] # day and night
}
Survive = {
    9 : [3, 4, 6, 7, 8] # day and night
}

'''Generation'''
iteratons = 250
