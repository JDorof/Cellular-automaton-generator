import Generator
# import FullGenerator as fg
import time
import numpy as np

'''Генерация'''

start = time.time()

print(f"{Generator.SeedClass.seed=}")
# Generator.SeedClass.ChangeSeed('1732886636.0177343')

sizes = (100, 100)
directory = ""

mask = np.array([[1  if ((x-49)**2 + (y-49)**2 <= 400) else 0 for x in range(100)] for y in range(100)])


field = Generator.InitializeField([10, 1], sizes)
field = Generator.RunAutomaton(field,10,1,[3, 6, 7, 8], [3, 4, 6, 7, 8],150,Generator.NeighborhoodClass.moore_neighborhood_1order)
field = Generator.MedianFilter(field, kernel_size=5, iterations=2, mask = mask)
# field = Generator.RunAutomaton(field,10,1,[3, 6], [3, 4, 6],200,Generator.NeighborhoodClass.moore_neighborhood_1order,mask=mask)

# print("10 = ", sum([1 for y in range(field.shape[0]) for x in range(field.shape[1]) if field[y][x] == 10]), " | 1 = ", sum([1 for y in range(field.shape[0]) for x in range(field.shape[1]) if field[y][x] == 1]))

'''Сохранение результата'''

Generator.SaveImage(field, directory + f"picture.png", Generator.GradientClass.black_orange_yellow_white)
# Generator.SaveImage(mask, directory + f"mask.png", [x for x in reversed(Generator.GradientClass.black_orange_yellow_white)])
# Generator.SaveMatrix(field1, directory + "matrix.txt")
# Generator.SaveCode("main.py", directory + "log.py")

print(start - time.time())
# Generator.SeedClass.seed = '1725972811.5725281'




