import time

start = time.time()

from PIL import Image
import numpy as np
from random import randint

# Связи с другими файлами
import rules
import blur_types
import Generator

im = Image.new('RGB', (rules.width, rules.height))
im2 = Image.new('RGB', (rules.width + 2, rules.height + 2))
im3 = Image.new('RGB', (rules.width, rules.height))

field = np.array([rules.chances[randint(0, len(rules.chances) - 1)] for i in range(rules.height * rules.width)], dtype="int32").reshape(rules.width, rules.height)

'''Сделать маштабируемый блюр и расширение спрайта''' # TODO




field = Generator.Generate(field, 10, 1, 200, rules.moore_neighborhood_1order)
# field = Generator.Shuffle_field(field, [9], [10], 5)
# field = Generator.Generate(field, 9, 10, 150, rules.moore_neighborhood_1order)

for i in range(5):
    field = Generator.Blur(field, blur_type=blur_types.cross_3x3)


field = Generator.Shuffle_field(field, [9], [10], 4)
field = Generator.Generate(field, 9, 10, 25, rules.moore_neighborhood_1order)

for i in range(2):
    field = Generator.Blur(field, blur_type=blur_types.cross_3x3, field_types={8, 9, 10})



field = Generator.Shuffle_field(field, [3], {1}, 4)
field = Generator.Generate(field, 3, 1, 25, rules.moore_neighborhood_1order)

for i in range(2):
    field = Generator.Blur(field, blur_type=blur_types.cross_3x3, field_types={1, 2, 3})


result = list(field.reshape(rules.height*rules.width))

for cell_type in range(1, 11):
    print(f'type {cell_type} = {result.count(cell_type)}')


for i in range(rules.width * rules.height):
    result[i] = rules.gradient[result[i] - 1]

im.putdata(result)
im.save(f'results/picture.png')

end = time.time()
print(end - start)
