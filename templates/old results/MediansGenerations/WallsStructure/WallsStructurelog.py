import Generator
import time
import numpy as np

'''Генерация'''


start = time.time()

print(f"{Generator.SeedClass.seed=}")

directory = "templates\old results\MediansGenerations\WallsStructure"

BirthDaN = [3, 6, 7, 8]
SurviveDaN = [3, 4, 6, 7, 8]

sizes = (300, 300)

field = Generator.InitializeField([10, 1], sizes)
field = Generator.MedianFilter(field, 5, iterations=10)

field = Generator.Blur(field, Generator.BlurClass.standart3x3, iterations=1)
field = Generator.ReplaceCells(field, [10], [1])
field = Generator.ReplaceCells(field, [9,8,7,6,5,4,3,2,], [10])
field = Generator.Blur(field, Generator.BlurClass.standart5x5, iterations=5)
field = Generator.MedianFilter(field, 7, target_values={1}, iterations=10)

for _ in range(3):
    field = Generator.ReplaceCells(field, [9,8,7,6,5,4,3,2,], [10])

    field = Generator.Blur(field, Generator.BlurClass.standart3x3, iterations=1)
    field = Generator.ReplaceCells(field, [10], [1])
    field = Generator.ReplaceCells(field, [9,8,7,6,5,4,3,2,], [10])
    field = Generator.Blur(field, Generator.BlurClass.standart5x5, iterations=5)
    field = Generator.MedianFilter(field, 7, target_values={1}, iterations=10)

field = Generator.ReplaceCells(field, [9,8,7,6,5], [10])
field = Generator.Blur(field, Generator.BlurClass.standart5x5, iterations=5)
field = Generator.MedianFilter(field, 11, target_values={1}, iterations=10)

field = Generator.ReplaceCells(field, [2], [10])
field = Generator.Blur(field, Generator.BlurClass.standart5x5, iterations=5)


print(time.time() - start)


'''Сохранение результата'''

Generator.SaveImage(field, directory + f"picture.png", Generator.GradientClass.black_orange_yellow_white)
Generator.SaveCode("main.py", directory + "log.py")




# Generator.SeedClass.seed = '1732309229.315991'