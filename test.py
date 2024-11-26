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

fg.SeedClass.ChangeSeed("011")

sizes = (50, 50)
BirthDaN = [3, 6, 7, 8]
SurviveDaN = [3, 4, 6, 7, 8]
iterations = 100


mask = [[x%2 for x in range(sizes[1])] for y  in range(sizes[0])]

field1 = fg.InitializeField([1, 9], sizes)



Generator.SaveMatrix(field1, "matrix1.md")
field1 = fg.RunAutomaton(field1, 9, 1, BirthDaN, SurviveDaN, iterations, fg.NeighborhoodClass.moore_neighborhood_1order)
field1 = fg.Blur(field1, fg.BlurClass.cross, iterations=3)
field1 = fg.MedianFilter(field1, 5, iterations=3, target_values=[1])


SaveImage(field1, "picture1.png", Generator.GradientClass.black_orange_yellow_white)



field2 = Generator.LoadMatrix("matrix1.md")
field2 = Generator.RunAutomaton(field2, 9, 1, BirthDaN, SurviveDaN, iterations, Generator.NeighborhoodClass.moore_neighborhood_1order)
field2 = Generator.Blur(field2, Generator.BlurClass.cross, iterations=3)
field2 = Generator.MedianFilter(field2, 5, iterations=3, target_values={1})



Generator.SaveImage(field2, "picture2.png", Generator.GradientClass.black_orange_yellow_white)

