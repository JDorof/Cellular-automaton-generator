import Generator
import time
import numpy as np

'''Генерация'''

start = time.time()

print(f"{Generator.SeedClass.seed=}")

sizes = (50, 50)
directory = "results/"

BirthDaN = [2, 1]
SurviveDaN = [1, 2]

field = Generator.InitializeField([10, 1], sizes)
field = Generator.RunAutomaton(field, 10, 1, BirthDaN, SurviveDaN, 50, Generator.NeighborhoodClass.plus)
field = Generator.RunAutomaton(field, 10, 1, [3, 4], [1, 2, 3, 4, 5], 10, Generator.NeighborhoodClass.plus)

'''Сохранение результата'''

Generator.SaveImage(field, directory + f"picture.png", Generator.GradientClass.black_orange_yellow_white)
Generator.SaveMatrix(field, directory + "matrix.txt")
Generator.SaveCode("main.py", directory + "log.py")

end = time.time()

print(end-start)
# Generator.SeedClass.seed = '1725709225.8854709'