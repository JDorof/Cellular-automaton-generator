import Generator

Generator.seed = '1725650929.6804326'
'''Генерация'''

sizes = (200, 200)
directory = "results/res/"

field = Generator.InitializeField([10] + [1 for _ in range(199)], sizes)
field = Generator.RunAutomaton(field, 10, 1, [1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8], 1, Generator.NeighborhoodClass.moore_neighborhood_1order)
for i in [8, 8, 9, 9, 10]:
    field = Generator.ReplaceCells(field, [1], [i], p=0.01)
    field = Generator.RunAutomaton(field, i, 1, [1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8], 1, Generator.NeighborhoodClass.moore_neighborhood_1order)
    field = Generator.Blur(field, Generator.BlurClass.down, target_values={4, 5, 6, 7, 8, 9, 10}, iterations=3)
for i in [10, 10, 10, 10, 8, 8, 7]:
    field = Generator.ReplaceCells(field, [1], [i], p=0.01)
    field = Generator.RunAutomaton(field, i, 1, [1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8], 1, Generator.NeighborhoodClass.moore_neighborhood_1order)
    field = Generator.Blur(field, Generator.BlurClass.down, target_values={8, 9, 10}, iterations=3)

'''Сохранение результата'''

Generator.SaveImage(field, directory + "picture.png", Generator.GradientClass.grass)
Generator.SaveMatrix(field, directory + "matrix.txt")
Generator.SaveCode("main.py", "results/res/log.py")
