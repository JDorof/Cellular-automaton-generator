import Generator
import time
import numpy as np

'''Генерация'''

# B35678/S5678 - Диамёба

start = time.time()

# Generator.SeedClass.ChangeSeed('1725972406.9964516')
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

# for i in range(5):
#     Generator.SaveImage(field, directory + f"picture{i}.png", Generator.GradientClass.all_gradients[i])
gradient = Generator.GradientClass.black_orange_yellow_white
gradient.reverse()
Generator.SaveImage(field, directory + f"picture.png", gradient)
Generator.SaveMatrix(field, directory + "matrix.txt")
Generator.SaveCode("main.py", directory + "log.py")

print(time.time() - start)