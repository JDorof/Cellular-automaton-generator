import Generator

Generator.seed = '1725650518.195272'

'''Генерация'''

sizes = (200, 200)
directory = "results/res/"

field = Generator.InitializeField([10, 1], sizes)
for _ in range(2):
    field = Generator.RunAutomaton(field, 10, 1, [3, 6, 7, 8], [3, 4, 6, 7, 8], 250, Generator.NeighborhoodClass.moore_neighborhood_1order)
    field = Generator.Blur(field, blur_type=Generator.BlurClass.standart3x3, target_values=[1], iterations=20)
    field = Generator.ReplaceCells(field, replace=[1, 2], to=[7, 8, 9], p=0.05)
    field = Generator.Blur(field, blur_type=Generator.BlurClass.standart5x5, iterations=10)
field = Generator.ReplaceCells(field, replace=[10], to=[1, 2], p=1)
field = Generator.Blur(field, blur_type=Generator.BlurClass.standart5x5, iterations=5)

'''Сохранение результата'''

Generator.SaveImage(field, directory + "picture.png", [x for x in reversed(Generator.GradientClass.ocean_beach_forest)])
Generator.SaveMatrix(field, directory + "matrix.txt")
Generator.SaveCode("main.py", "results/res/log.py")
