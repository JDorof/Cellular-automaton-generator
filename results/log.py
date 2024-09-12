import Generator
import time
import numpy as np

'''Генерация'''


start = time.time()

print(f"{Generator.SeedClass.seed=}")

sizes = (100, 100)
directory = "results/"

fields = []

BirthDaN = [6, 5, 4 ,3]
SurviveDaN = [7, 6, 5]
a = 1

field = Generator.InitializeField([10, 1], sizes)
field = Generator.Blur(field, Generator.BlurClass.plus, iterations=2)
field2 = Generator.InitializeField([10, 1], (1000, 1000))
field2 = Generator.Blur(field2, Generator.BlurClass.plus, iterations=2)
field = Generator.UpScale(field, scale=10)
field = Generator.AverageAmountOfFields(field, field2)

'''Сохранение результата'''

gradient = Generator.GradientClass.black_orange_yellow_white
gradient.reverse()
Generator.SaveImage(field, directory + f"picture.png", gradient)
Generator.SaveMatrix(field, directory + "matrix.txt")
Generator.SaveCode("main.py", directory + "log.py")

print(time.time() - start)
# Generator.SeedClass.seed = '1726157149.7274232'