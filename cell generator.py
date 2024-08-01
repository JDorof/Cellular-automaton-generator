from PIL import Image
import numpy as np
from random import randint, shuffle

# Связи с другими файлами
import rules
from values import *

im = Image.new('RGB', (width, heigth))

'''крч идея сделать градиенты, а все расчеты проводить с numpy с числами от 0 до 9, или другой диапозон.
Потом, в зависимости от числа подставлять в финальную картинку тот или иной цвет''' # TODO

# field = [[0, 0, 0, 0, 0], [0, 1, 0, 0, 0],[ 0, 1, 0, 0, 0],[ 0, 1, 0, 0, 0],[ 0, 0, 0, 0, 0]] // Че-то ему не нравится в обычныйх массивах
# field = np.array([0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]).reshape(heigth, width) // хотя вот это считает правильно

number_list = [0, 0, 0, 1, 1]

field = np.array([number_list[randint(0, len(number_list) - 1)] for x in range(heigth * width)]).reshape(width, heigth)
new_field = field.copy()

for i in range (201):

    print(f"i={i}", end=" ")

    for x in range(width):
        for y in range(heigth):
            rules.DayAndNight(x, y, field, new_field, width, heigth, 1)

    field = new_field.copy()


im.putdata([white if i == 1 else black for row in new_field for i in row])
im.save(f'cells generator/picture.png')
