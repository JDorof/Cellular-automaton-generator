import Generator

'''Генерация'''

Generator.SeedClass.ChangeSeed("aboba")
print(f"{Generator.SeedClass.seed=}")

sizes = (200, 200)
directory = "results/"

BirthDaN = [3, 4]
SurviveDaN = [3, 4]

field = Generator.InitializeField([10, 1], sizes)
field = Generator.RunAutomaton(field, 10, 1, BirthDaN, SurviveDaN, 10, Generator.NeighborhoodClass.cross)
field = Generator.RunAutomaton(field, 10, 1, [4], [0, 1, 2, 3, 4, 5], 1, Generator.NeighborhoodClass.plus)
field = Generator.RunAutomaton(field, 10, 1, [2], [0, 1, 2, 3, 4, 5], 1, Generator.NeighborhoodClass.plus)
field = Generator.Blur(field, Generator.BlurClass.cross, iterations=4)
field = Generator.ReplaceCells(field, [1], [10, 9])
field = Generator.ReplaceCells(field, [2], [1])
field = Generator.Blur(field, Generator.BlurClass.cross, target_values={2, 3, 4, 5, 6, 7, 8, 9, 10}, iterations=4)
field = Generator.ReplaceCells(field, [1], [10, 9])
field = Generator.Blur(field, Generator.BlurClass.cross, target_values={9, 10}, iterations=1)

'''Сохранение результата'''

for i in range(5):
    Generator.SaveImage(field, directory + f"picture{i}.png", Generator.GradientClass.all_gradients[i])
Generator.SaveMatrix(field, directory + "matrix.txt")
Generator.SaveCode("main.py", directory + "log.py")

# Generator.SeedClass.seed = 'aboba'