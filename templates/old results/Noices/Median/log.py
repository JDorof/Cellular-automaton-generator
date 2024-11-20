import Generator
import time
import numpy as np

'''Генерация'''


start = time.time()

print(f"{Generator.SeedClass.seed=}")

directory = "templates/old results/Noices/Median/"

BirthDaN = [3, 6, 7, 8]
SurviveDaN = [3, 4, 6, 7, 8]

sizes = (200, 200)

field = Generator.InitializeField([10, 1], sizes)


field = Generator.MedianFilter(field, 5, iterations=10)
field = Generator.Blur(field, Generator.BlurClass.cross, target_values={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, iterations=10)
field = Generator.MedianFilter(field, 5, iterations=10)


print(time.time() - start)



'''Сохранение результата'''

Generator.SaveImage(field, directory + f"picture.png", Generator.GradientClass.black_orange_yellow_white)
Generator.SaveCode("main.py", directory + "log.py")




# Generator.SeedClass.seed = '1732101938.8555338'