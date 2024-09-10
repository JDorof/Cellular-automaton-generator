import Generator
import time
import numpy as np

'''Генерация'''


start = time.time()

print(f"{Generator.SeedClass.seed=}")

sizes = (200, 200)
directory = "results/"

fields = []


BirthDaN = [6, 5, 4 ,3]
SurviveDaN = [7, 6, 5]
a = 3


for x in range(a):
    field = Generator.InitializeField([10, 1], sizes)
    field = Generator.RunAutomaton(field, 10, 1, BirthDaN, SurviveDaN, 5, np.logical_or(Generator.NeighborhoodClass.cross,  Generator.NeighborhoodClass.horizontal).astype("int32"))
    fields.append(field)

field = Generator.AverageAmountOfFields(*fields)
field = Generator.Blur(field, Generator.BlurClass.standart5x5, iterations=1)

'''Сохранение результата'''

gradient = Generator.GradientClass.ocean_beach_forest
gradient.reverse()
Generator.SaveImage(field, directory + f"picture3.png", gradient)
Generator.SaveMatrix(field, directory + "matrix.txt")
Generator.SaveCode("main.py", directory + "log.py")

print(time.time() - start)
# Generator.SeedClass.seed = '1725973660.317327'