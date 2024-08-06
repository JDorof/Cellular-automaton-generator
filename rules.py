import gradients

'''Image'''
height = 100
width = 100

'''Colors'''
counter = 10
chances = [0, 9]
gradient = gradients.ocean_beach_forest
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
    9 : [3, 6, 7, 8], # day and night for moore
    8 : [3, 6, 7, 8], # day and night for moore
    0 : [3, 6, 7, 8] # day and night for moore
}
Survive = {
    9 : [3, 4, 6, 7, 8], # day and night for moore
    8 : [3, 4, 6, 7, 8], # day and night for moore
    0 : [3, 4, 6, 7, 8] # day and night for moore
}

'''Blur types''' # сумма всех элементов должа быть равна 1
blur_3x3 = [
        [0.0625, 0.125, 0.0625],
        [0.125, 0.25, 0.125],
        [0.0625, 0.125, 0.0625]
    ]

blur_cross = [
        [0.15, 0.0, 0.15],
        [0.0, 0.4, 0.0],
        [0.15, 0.0, 0.15]
    ]




# '''Generation'''
# iteratons = 250
