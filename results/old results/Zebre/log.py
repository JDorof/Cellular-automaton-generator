import Generator
import time
import numpy as np

'''Генерация'''

start = time.time()

print(f"{Generator.SeedClass.seed=}")
print(np.logical_or(Generator.NeighborhoodClass.cross,  Generator.NeighborhoodClass.horizontal).astype("int32"))

sizes = (200, 200)
directory = "results/"

BirthDaN = [6, 5, 4 ,3]
SurviveDaN = [7, 6, 5]

field = Generator.InitializeField([10, 1], sizes)
field = Generator.RunAutomaton(field, 10, 1, BirthDaN, SurviveDaN, 5, np.logical_or(Generator.NeighborhoodClass.cross,  Generator.NeighborhoodClass.horizontal).astype("int32"))
# field = Generator.Blur(field, Generator.BlurClass.standart3x3, iterations=3)

'''Сохранение результата'''

Generator.SaveImage(field, directory + f"picture.png", Generator.GradientClass.black_orange_yellow_white)
Generator.SaveMatrix(field, directory + "matrix.txt")
Generator.SaveCode("main.py", directory + "log.py")

end = time.time()

print(end-start)
# Generator.SeedClass.seed = '1725708295.4370253'