import time

start = time.time()

from PIL import Image
import numpy as np
from random import randint

# Связи с другими файлами
import rules
import Generator

im = Image.new('RGB', (rules.width, rules.height))

'''крч идея сделать градиенты, а все расчеты проводить с numpy с числами от 0 до 9, или другой диапозон.
Потом, в зависимости от числа подставлять в финальную картинку тот или иной цвет''' # TODO

'''Оптимизация: не передавать в параметрах каждый раз поле, ширину, высоту и тп.''' # TODO

# for i in range(3):
#     for y in range(height):
#         for x in range(width):
#             if field[y][x] == 2:
#                 new_field[y][x] = 2
#                 continue
#             if field[y][x] == 1:
#                 new_field[y][x] = 1
#                 continue
#             if old_rules.AliveInMooreNeighborhood(x, y, field, width, height, 2) > 0:
#                 new_field[y][x] = 1
#                 continue
#             if old_rules.AliveInMooreNeighborhood(x, y, field, width, height, 1) > 2:
#                 if randint(0, 1) == 1:
#                     new_field[y][x] = 1
#                     continue
#             new_field[y][x] = 0
            
#     field = new_field

field = Generator.Generate()

result = list(field.reshape(rules.height*rules.width))

for i in range(rules.width * rules.height):
    result[i] = rules.gradient[result[i]]

im.putdata(result)
im.save(f'results/picture.png')

end = time.time()
print(end - start)
