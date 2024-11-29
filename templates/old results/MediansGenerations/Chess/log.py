import Generator
import time
import numpy as np

'''Генерация'''

start = time.time()

print(f"{Generator.SeedClass.seed=}")

sizes = (100, 100)
directory = "templates/old results/MediansGenerations/Chess/"


field = Generator.InitializeField([10, 1], sizes)

field = Generator.MedianFilter(field, kernel_mask=Generator.NeighborhoodClass.cross_1order, iterations=5, mode="mask")
field = Generator.MedianFilter(field, kernel_mask=Generator.NeighborhoodClass.plus, iterations=5, mode="mask")


'''Сохранение результата'''

Generator.SaveImage(field, directory + f"picture.png", [x for x in reversed(Generator.GradientClass.black_orange_yellow_white)])
Generator.SaveCode("main.py", directory + "log.py")

print(start - time.time())





# Generator.SeedClass.seed = '1732896763.8101885'