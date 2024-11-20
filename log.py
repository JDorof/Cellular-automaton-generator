import Generator
import time
import numpy as np

'''Генерация'''


start = time.time()

print(f"{Generator.SeedClass.seed=}")

directory = ""

BirthDaN = [3, 6, 7, 8]
SurviveDaN = [3, 4, 6, 7, 8]

sizes = (200, 200)

field = Generator.InitializeField([10, 1], sizes)
field = Generator.RunAutomaton(field, 10, 1, BirthDaN, SurviveDaN, 200, Generator.NeighborhoodClass.moore_neighborhood_1order)
field = Generator.ReplaceCells(field, replace=[1], to=[3], p=0.5)
field = Generator.RunAutomaton(field, 3, 1, BirthDaN, SurviveDaN, 25, Generator.NeighborhoodClass.moore_neighborhood_1order)
field = Generator.ReplaceCells(field, replace=[10], to=[8], p=0.5)
field = Generator.RunAutomaton(field, 8, 10, BirthDaN, SurviveDaN, 25, Generator.NeighborhoodClass.moore_neighborhood_1order)
field = Generator.ReplaceCells(field, replace=[10], to=[1], p=1)
field = Generator.Blur(field, Generator.BlurClass.cross, target_values={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, iterations=30)
field = Generator.ReplaceCells(field, replace=[5, 6, 7, 8], to=[9], p=0.9)
field = Generator.Blur(field, Generator.BlurClass.cross, target_values={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, iterations=30)

'''Сохранение результата'''

Generator.SaveImage(field, directory + "picture.png", Generator.GradientClass.ocean_beach_forest)

print(time.time() - start)



'''Сохранение результата'''

Generator.SaveImage(field, directory + f"picture.png", Generator.GradientClass.black_orange_yellow_white)
Generator.SaveCode("main.py", directory + "log.py")




# Generator.SeedClass.seed = '1732031540.2479453'