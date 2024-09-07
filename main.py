import Generator

'''Генерация'''


Generator.SeedClass.ChangeSeed("aboba")
print(f"{Generator.SeedClass.seed=}")


sizes = (100, 100)
directory = "results/"

BirthDaN = [3, 4]
SurviveDaN = [3, 4]

field = Generator.InitializeField([10, 1], sizes)
field = Generator.RunAutomaton(field, 10, 1, BirthDaN, SurviveDaN, 200, Generator.NeighborhoodClass.cross)
field = Generator.RunAutomaton(field, 10, 1, [4], [0, 1, 2, 3, 4, 5], 1, Generator.NeighborhoodClass.plus)
field = Generator.RunAutomaton(field, 10, 1, [2], [0, 1, 2, 3, 4, 5], 1, Generator.NeighborhoodClass.plus)
field = Generator.Blur(field, Generator.BlurClass.cross, iterations=5)
# field = Generator.Blur(field, Generator.BlurClass.standart3x3, iterations=5)

'''Сохранение результата'''

Generator.SaveImage(field, directory + "picture.png", Generator.GradientClass.black_to_white)
Generator.SaveMatrix(field, directory + "matrix.txt")
Generator.SaveCode("main.py", directory + "log.py")
