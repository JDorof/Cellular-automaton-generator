import Generator
import time
import numpy as np

'''Генерация'''

# B35678/S5678 - Диамёба
# B3678/S34678 - День и ночь

start = time.time()

Generator.SeedClass.ChangeSeed('1732048593.5517836')
print(f"{Generator.SeedClass.seed=}")

directory = "templates/old results/Rivers or Caves/Concatenation/"

BirthDaN = [3, 6, 7, 8]
SurviveDaN = [3, 4, 6, 7, 8]

# sizes = (1000, 1000)

# field1 = Generator.InitializeField([10, 1], sizes)
# field1 = Generator.MedianFilter(field1, 5, iterations=5)
# field1 = Generator.Blur(field1, Generator.BlurClass.cross, target_values={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, iterations=5)
# field1 = Generator.MedianFilter(field1, 5, iterations=5)

# field2 = Generator.InitializeField([10, 1], (200,200))
# for _ in range(2):
#     field2 = Generator.RunAutomaton(field2, 10, 1, [3, 6, 7, 8], [3, 4, 6, 7, 8], 250, Generator.NeighborhoodClass.moore_neighborhood_1order)
#     field2 = Generator.Blur(field2, blur_type=Generator.BlurClass.standart3x3, target_values=[1], iterations=10)
#     field2 = Generator.ReplaceCells(field2, replace=[1, 2], to=[7, 8, 9], p=0.05)
#     field2 = Generator.Blur(field2, blur_type=Generator.BlurClass.standart5x5, iterations=10)
# field2 = Generator.ReplaceCells(field2, replace=[10], to=[1, 2], p=1)
# field2 = Generator.Blur(field2, blur_type=Generator.BlurClass.standart5x5, iterations=5)

# field2 = Generator.UpScale(field2, 5)

# mask = np.isin(field2, [10, 9, 8,7,6,5,4])

# # field3 = Generator.ReplaceCells(field1, range(1,11), [1,2,3])
# field3 = Generator.ReplaceCells(field1, range(1,11), [1], mask=mask)
# field3 = Generator.MedianFilter(field3, 5, iterations=5)

# # field3 = Generator.AverageAmountOfFields(field1, field3, field3, field3, field3, field3)
# field3 = Generator.Blur(field3, blur_type=Generator.BlurClass.standart5x5, iterations=5)


matrix = np.array([[0,0,0,0,0],[0,0,0,0,0],[0,0,1000,0,0,],[0,0,0,0,0],[0,0,0,0,0]])
print(matrix)

matrix1 = Generator.Blur(matrix, Generator.BlurClass.standart3x3, target_values=set(range(1,1001)) , iterations=4)

print(matrix)
print(matrix1)


print(time.time() - start)


'''Сохранение результата'''

# Generator.SaveImage(field1, directory + f"picture1.png", Generator.GradientClass.black_orange_yellow_white)
# Generator.SaveImage(field2, directory + f"picture2.png", Generator.GradientClass.black_orange_yellow_white)
# Generator.SaveImage(field3, directory + f"picture3.png", Generator.GradientClass.black_orange_yellow_white)
# Generator.SaveMatrix(field, directory + "matrix.txt")
Generator.SaveCode("main.py", directory + "log.py")



