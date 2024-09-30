import Generator
import time
import numpy as np

'''Генерация'''


start = time.time()

Generator.SeedClass.ChangeSeed('0')
print(f"{Generator.SeedClass.seed=}")

sizes = (100, 100)
directory = "results/"

field = Generator.InitializeField([10, 1, 1, 1, 1], (200, 200))
for i in range(200):
    field = Generator.UpdateField(field, 10, 1, [1, 2], [1, 2, 3], Generator.NeighborhoodClass.horizontal_1order
                                   , birth_chance=1, survive_chance=1, death_chance=1)
    field = Generator.UpdateField(field, 10, 1, [1, 2], [1, 2, 3], Generator.NeighborhoodClass.vertical_2order
                                   , birth_chance=1, survive_chance=1, death_chance=1)
field = Generator.Blur(field, Generator.BlurClass.cross, iterations=5)

print(time.time() - start)



'''Сохранение результата'''

Generator.SaveImage(field, directory + f"picture.png", Generator.GradientClass.black_orange_yellow_white)
Generator.SaveCode("main.py", directory + "log.py")




# Generator.SeedClass.seed = '0'