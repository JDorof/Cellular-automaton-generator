import Generator
import time
import numpy as np

'''Генерация'''

# B35678/S5678 - Диамёба

start = time.time()

# Generator.SeedClass.ChangeSeed('1725972406.9964516')
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
field = Generator.Blur(field, Generator.BlurClass.standart3x3, iterations=1)

'''Сохранение результата'''

# for i in range(5):
#     Generator.SaveImage(field, directory + f"picture{i}.png", Generator.GradientClass.all_gradients[i])
gradient = Generator.GradientClass.ocean_beach_forest
gradient.reverse()
Generator.SaveImage(field, directory + f"picture3.png", gradient)
Generator.SaveMatrix(field, directory + "matrix.txt")
Generator.SaveCode("main.py", directory + "log.py")

print(time.time() - start)