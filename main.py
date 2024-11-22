import Generator
import time
import numpy as np

'''Генерация'''

# B35678/S5678 - Диамёба
# B3678/S34678 - День и ночь

start = time.time()

# Generator.SeedClass.ChangeSeed('1732048593.5517836')
print(f"{Generator.SeedClass.seed=}")

directory = ""

BirthDaN = [3, 6, 7, 8]
SurviveDaN = [3, 4, 6, 7, 8]

sizes = (300, 300)

field = Generator.InitializeField([10, 1], sizes)

print(time.time() - start)


'''Сохранение результата'''

Generator.SaveImage(field, directory + f"picture.png", Generator.GradientClass.black_orange_yellow_white)
# Generator.SaveMatrix(field, directory + "matrix.txt")
# Generator.SaveCode("main.py", directory + "log.py")



