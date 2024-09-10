import Generator
import time
import numpy as np

'''Генерация'''


start = time.time()

print(f"{Generator.SeedClass.seed=}")

sizes = (200, 200)
directory = "results/"

fields = []

for x in range(2):
    field1 = Generator.InitializeField([10, 1], sizes)
    for _ in range(2):
        field1 = Generator.RunAutomaton(field1, 10, 1, [3, 6, 7, 8], [3, 4, 6, 7, 8], 250, Generator.NeighborhoodClass.moore_neighborhood_1order)
        field1 = Generator.Blur(field1, blur_type=Generator.BlurClass.standart3x3, target_values=[1], iterations=20)
        field1 = Generator.ReplaceCells(field1, replace=[1, 2], to=[7, 8, 9], p=0.05)
        field1 = Generator.Blur(field1, blur_type=Generator.BlurClass.standart5x5, iterations=10)
    field1 = Generator.ReplaceCells(field1, replace=[10], to=[1, 2], p=1)
    field1 = Generator.Blur(field1, blur_type=Generator.BlurClass.standart5x5, iterations=5)
    fields.append(field1)

for x in range(1):
    field1 = Generator.InitializeField([10, 1], sizes)
    for _ in range(2):
        field1 = Generator.RunAutomaton(field1, 10, 1, [3, 6, 7, 8], [3, 4, 6, 7, 8], 1000, Generator.NeighborhoodClass.moore_neighborhood_1order)
        field1 = Generator.Blur(field1, blur_type=Generator.BlurClass.standart3x3, target_values=[1], iterations=20)
        field1 = Generator.ReplaceCells(field1, replace=[1, 2], to=[7, 8, 9], p=0.05)
        field1 = Generator.Blur(field1, blur_type=Generator.BlurClass.standart5x5, iterations=10)
    fields.append(field1)

field3 = Generator.AveragedSumOfFields(*fields)


'''Сохранение результата'''

Generator.SaveImage(field3, directory + f"picture3.png", Generator.GradientClass.black_orange_yellow_white)
Generator.SaveMatrix(field1, directory + "matrix.txt")
Generator.SaveCode("main.py", directory + "log.py")

print(start - time.time())
# Generator.SeedClass.seed = '1725971663.4680452'