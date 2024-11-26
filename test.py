import FullGenerator as fg
import Generator
from PIL import Image
import numpy as np

def SaveImage(field: list, path: str, gradient: list):
    sizes = (len(field), len(field[0]))
    im = Image.new('RGB', sizes)
    result = [field[y][x] for y in range(sizes[0]) for x in range(sizes[1])]
    try:
        for i in range(sizes[0] * sizes[1]):
            result[i] = gradient[result[i] - 1]
    except IndexError:
        print("SaveImage function:")
        print(f"ERROR: You have int values bigger than 'max index - 1': {result[i] - 1}")
        exit()
    im.putdata(result)
    im.save(path)

# fg.SeedClass.ChangeSeed("01")

sizes = (50, 50)
BirthDaN = [3, 6, 7, 8]
SurviveDaN = [3, 4, 6, 7, 8]
iterations = 100


field1 = fg.InitializeField([1, 9], sizes)
field2 = fg.InitializeField([1, 9], sizes)
field3 = fg.InitializeField([1, 9], sizes)

Generator.SaveMatrix(field1, "matrix1.md")
Generator.SaveMatrix(field2, "matrix2.md")
Generator.SaveMatrix(field3, "matrix3.md")

field1 = fg.RunAutomaton(field1, 9, 1, BirthDaN, SurviveDaN, iterations, fg.NeighborhoodClass.moore_neighborhood_1order)
field2 = fg.RunAutomaton(field2, 9, 1, BirthDaN, SurviveDaN, iterations, fg.NeighborhoodClass.moore_neighborhood_1order)
field3 = fg.RunAutomaton(field3, 9, 1, BirthDaN, SurviveDaN, iterations, fg.NeighborhoodClass.moore_neighborhood_1order)

field = fg.AverageAmountOfFields(field1, field2, field3)

SaveImage(field, "picture1.png", Generator.GradientClass.black_orange_yellow_white)

field1 = Generator.LoadMatrix("matrix1.md")
field2 = Generator.LoadMatrix("matrix2.md")
field3 = Generator.LoadMatrix("matrix3.md")

field1 = Generator.RunAutomaton(field1, 9, 1, BirthDaN, SurviveDaN, iterations, Generator.NeighborhoodClass.moore_neighborhood_1order)
field2 = Generator.RunAutomaton(field2, 9, 1, BirthDaN, SurviveDaN, iterations, Generator.NeighborhoodClass.moore_neighborhood_1order)
field3 = Generator.RunAutomaton(field3, 9, 1, BirthDaN, SurviveDaN, iterations, Generator.NeighborhoodClass.moore_neighborhood_1order)

field = Generator.AverageAmountOfFields(field1, field2, field3)

Generator.SaveImage(field, "picture2.png", Generator.GradientClass.black_orange_yellow_white)

