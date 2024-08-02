from PIL import Image
import numpy as np
from random import randint, shuffle

# Связи с другими файлами
import rules
from values import *

im = Image.new('RGB', (width, heigth))

'''крч идея сделать градиенты, а все расчеты проводить с numpy с числами от 0 до 9, или другой диапозон.
Потом, в зависимости от числа подставлять в финальную картинку тот или иной цвет''' # TODO

'''Оптимизация: не передавать в параметрах каждый раз поле, ширину, высоту и тп.''' # TODO

number_list = [0, 0, 0, 2, 2]
# number_list = [0, 2]

field = np.array([number_list[randint(0, len(number_list) - 1)] for x in range(heigth * width)]).reshape(width, heigth)
# print(field.dtype) int32
new_field = field.copy()

for i in range(201):

    for y in range(heigth):
        for x in range(width):
            rules.DayAndNight(x, y, field, new_field, width, heigth, 2)

    field = new_field.copy()

for i in range(3):
    for y in range(heigth):
        for x in range(width):
            if field[y][x] == 2:
                new_field[y][x] = 2
                continue
            if field[y][x] == 1:
                new_field[y][x] = 1
                continue
            if rules.AliveInMooreNeighborhood(x, y, field, width, heigth, 2) > 0:
                new_field[y][x] = 1
                continue
            if rules.AliveInMooreNeighborhood(x, y, field, width, heigth, 1) > 2:
                if randint(0, 1) == 1:
                    new_field[y][x] = 1
                    continue
            new_field[y][x] = 0
            
    field = new_field

result = list(field.reshape(heigth*width))

for i in range(width * heigth):
        match result[i]:
            case 0:
                result[i] = black
            case 1:
                result[i] = grey
            case 2:
                result[i] = white



im.putdata(result)
im.save(f'results/picture.png')
