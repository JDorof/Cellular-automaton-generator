import time

start = time.time()

from PIL import Image
import numpy as np
from random import randint

# Связи с другими файлами
import rules
import Generator

im = Image.new('RGB', (rules.width, rules.height))
im2 = Image.new('RGB', (rules.width + 2, rules.height + 2))
im3 = Image.new('RGB', (rules.width, rules.height))

field = np.array([rules.chances[randint(0, len(rules.chances) - 1)] for x in range(rules.height * rules.width)], dtype="int32").reshape(rules.width, rules.height)

'''Сделать маштабируемый блюр и расширение спрайта''' # TODO

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

field = Generator.Generate(field, 9, 0, 200, rules.moore_neighborhood_1order)
# field = Generator.Shuffle_field(field, [8], [9], 5)
# field = Generator.Generate(field, 8, 9, 150, rules.moore_neighborhood_1order)
field = Generator.Blur(field)
field = Generator.Blur(field)
field = Generator.Blur(field)
field = Generator.Blur(field)
field = Generator.Blur(field)
# field = Generator.Shuffle_field(field, [8], [9], 4)

field = Generator.Generate(field, 8, 9, 25, rules.moore_neighborhood_1order)
field = Generator.Blur(field)


result = list(field.reshape(rules.height*rules.width))
print(f'{result.count(9) = }')
print(f'{result.count(0) = }')

for i in range(rules.width * rules.height):
    result[i] = rules.gradient[result[i]]

im.putdata(result)
im.save(f'results/picture.png')

end = time.time()
print(end - start)
