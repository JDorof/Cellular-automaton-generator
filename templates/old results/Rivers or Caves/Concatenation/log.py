import Generator
import time
import numpy as np

'''Генерация'''


start = time.time()

Generator.SeedClass.ChangeSeed('1732048593.5517836')
print(f"{Generator.SeedClass.seed=}")

directory = "templates/old results/Rivers or Caves/Concatenation/"

BirthDaN = [3, 6, 7, 8]
SurviveDaN = [3, 4, 6, 7, 8]









matrix = np.array([[0,0,0,0,0],[0,0,0,0,0],[0,0,1000,0,0,],[0,0,0,0,0],[0,0,0,0,0]])
print(matrix)

matrix1 = Generator.Blur(matrix, Generator.BlurClass.standart3x3, target_values=set(range(1,1001)) , iterations=4)

print(matrix)
print(matrix1)


print(time.time() - start)


'''Сохранение результата'''

Generator.SaveCode("main.py", directory + "log.py")




# Generator.SeedClass.seed = '1732048593.5517836'