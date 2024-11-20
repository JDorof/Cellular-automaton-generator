import Generator
import time
import numpy as np

'''Генерация'''


start = time.time()

print(f"{Generator.SeedClass.seed=}")

sizes = (100, 100)
directory = "results/"

gradient = Generator.GradientClass.black_orange_yellow_white
gradient.reverse()

field = Generator.InitializeField([10, 10, 1, 1, 1], sizes)
field = Generator.Blur(field, blur_type=Generator.BlurClass.cross, iterations=2)
field = Generator.UpScale(field, scale=10)
field1 = Generator.InitializeField([6, 1], (1000, 1000))
field = Generator.AverageAmountOfFields(field, field1)
field = Generator.Blur(field, blur_type=Generator.BlurClass.standart5x5, iterations=2)
Generator.SaveImage(field, directory + f"picture1.png", gradient)


field = Generator.InitializeField([10, 1], sizes)
field = Generator.Blur(field, Generator.BlurClass.plus, iterations=2)
field2 = Generator.InitializeField([10, 1], (1000, 1000))
field2 = Generator.Blur(field2, Generator.BlurClass.plus, iterations=2)
field = Generator.UpScale(field, scale=10)
field = Generator.AverageAmountOfFields(field, field2)
Generator.SaveImage(field, directory + f"picture2.png", gradient)


'''Сохранение результата'''

Generator.SaveCode("main.py", directory + "log.py")


print(time.time() - start)
# Generator.SeedClass.seed = '1726483830.0056472'