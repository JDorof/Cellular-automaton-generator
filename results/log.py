import Generator

Generator.seed = '1725691161.0298133'
'''Генерация'''

print(f"{Generator.seed=}")

sizes = (100, 100)
directory = "results/"

BirthDaN = [3, 6, 7, 8]
SurviveDaN = [3, 4, 6, 7, 8]

field = Generator.InitializeField([10, 1], sizes)
field = Generator.RunAutomaton(field, 10, 1, BirthDaN, SurviveDaN, 200, Generator.NeighborhoodClass.moore_neighborhood_1order)
field = Generator.Blur(field, Generator.BlurClass.cross, iterations=5)
field = Generator.Blur(field, Generator.BlurClass.standart3x3, iterations=5)

'''Сохранение результата'''

Generator.SaveImage(field, directory + "picture.png", Generator.GradientClass.black_to_white)
Generator.SaveMatrix(field, directory + "matrix.txt")
Generator.SaveCode("main.py", directory + "log.py")
