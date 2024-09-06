import Generator

'''Генерация'''

sizes = (200, 200)
directory = "results/"

BirthDaN = [3, 6, 7, 8]
SurviveDaN = [3, 4, 6, 7, 8]

field = Generator.InitializeField([10, 1], sizes)

field = Generator.RunAutomaton(field, 10, 1, BirthDaN, SurviveDaN, 200, Generator.NeighborhoodClass.standart3x3)

'''Сохранение результата'''

Generator.SaveImage(field, directory + "picture.png", Generator.GradientClass.grass)
Generator.SaveMatrix(field, directory + "matrix.txt")
Generator.SaveCode("main.py", directory + "log.py")
