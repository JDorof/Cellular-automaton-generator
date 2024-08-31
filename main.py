import rules
import blur_types
import Generator

from os import mkdir
import time
import logging

start = time.time()
logging.basicConfig(level=logging.INFO, filename=f'results/res/log.log', filemode="w")

# local_time = time.asctime().replace(':', '_')[4:19]
# mkdir(path=f'results/{local_time}')
# logging.basicConfig(level=logging.INFO, filename=f'results/{local_time}/log.log', filemode="w")

print(f'{rules.seed = }')

'''Генерация'''

# field = Generator.InitializeField([10, 10, 10, 1, 1], (rules.height, rules.width))


field = Generator.InitializeField([10] + [1 for _ in range(199)], (rules.height, rules.width))
# field = Generator.InitializeField([1], (rules.height, rules.width))
field = Generator.RunAutomaton(field, 10, 1, [1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8], 1, rules.moore_neighborhood_1order)
for i in [8, 8, 9, 9, 10]:
    field = Generator.ReplaceCells(field, replace=[1], to=[i], p=0.01)
    field = Generator.RunAutomaton(field, i, 1, [1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8], 1, rules.moore_neighborhood_1order)
    field = Generator.Blur(field, blur_types.down, target_values={4, 5, 6, 7, 8, 9, 10}, iterations=3)
for i in [10, 10, 10, 10, 8, 8, 7]:
    field = Generator.ReplaceCells(field, replace=[1], to=[i], p=0.01)
    field = Generator.RunAutomaton(field, i, 1, [1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8], 1, rules.moore_neighborhood_1order)
    field = Generator.Blur(field, blur_types.down, target_values={8, 9, 10}, iterations=3)
# field = Generator.Blur(field, blur_types.down, target_values={3, 4, 5, 6, 7, 8, 9, 10}, iterations=4)
    # field = Generator.Blur(field, blur_types.down_standart3x3, target_values={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, iterations=2)

# field = Generator.ReplaceCells(field, replace=[10], to=[7], p=1)
# field = Generator.ReplaceCells(field, replace=[7], to=[1], p=0.5)
# field = Generator.Blur(field, blur_types.standart3x3, target_values={7, 1}, iterations=10)


# field = Generator.InitializeField([10, 1], (rules.height, rules.width))
# field = Generator.RunAutomaton(field, 10, 1, [3, 6, 7, 8], [3, 4, 6, 7, 8], 200, rules.moore_neighborhood_1order)
# field = Generator.ReplaceCells(field, replace=[1], to=[3], p=0.5)
# field = Generator.RunAutomaton(field, 3, 1, [3, 6, 7, 8], [3, 4, 6, 7, 8], 25, rules.moore_neighborhood_1order)
# field = Generator.ReplaceCells(field, replace=[10], to=[8], p=0.5)
# field = Generator.RunAutomaton(field, 8, 10, [3, 6, 7, 8], [3, 4, 6, 7, 8], 25, rules.moore_neighborhood_1order)
# field = Generator.ReplaceCells(field, replace=[10], to=[1], p=1)
# field = Generator.Blur(field, blur_types.cross, target_values={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, iterations=30)
# field = Generator.ReplaceCells(field, replace=[5, 6, 7, 8], to=[9], p=0.9)
# field = Generator.Blur(field, blur_types.cross, target_values={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, iterations=30)


# field = Generator.InitializeField([9, 10], (rules.height, rules.width))
# field = Generator.RunAutomaton(field, 9, 10, 1000, rules.moore_neighborhood_1order)
# field = Generator.ReplaceCells(field, replace=[10], to=[1], p=0.5)
# for _ in range(2):
#     field = Generator.RunAutomaton(field, 10, 1, 250, rules.moore_neighborhood_1order)
#     field = Generator.Blur(field, blur_type=blur_types.standart3x3, target_values=[1], iterations=20)
#     # field = Generator.ReplaceCells(field, replace=[2, 3, 4, 5, 6, 7, 8, 9], to=[10])
#     field = Generator.ReplaceCells(field, replace=[1, 2], to=[7, 8, 9], p=0.05)
#     field = Generator.Blur(field, blur_type=blur_types.standart5x5, iterations=10)
# field = Generator.ReplaceCells(field, replace=[10], to=[1, 2], p=1)
# field = Generator.Blur(field, blur_type=blur_types.standart5x5, iterations=5)


# field = Generator.InitializeField([10, 1], (rules.height, rules.width))
# for _ in range(2):
#     field = Generator.RunAutomaton(field, 10, 1, [3, 6, 7, 8], [3, 4, 6, 7, 8], 250, rules.moore_neighborhood_1order)
#     field = Generator.Blur(field, blur_type=blur_types.standart3x3, target_values=[1], iterations=20)
#     # field = Generator.ReplaceCells(field, replace=[2, 3, 4, 5, 6, 7, 8, 9], to=[10])
#     field = Generator.ReplaceCells(field, replace=[1, 2], to=[7, 8, 9], p=0.05)
#     field = Generator.Blur(field, blur_type=blur_types.standart5x5, iterations=10)
# field = Generator.ReplaceCells(field, replace=[10], to=[1, 2], p=1)
# field = Generator.Blur(field, blur_type=blur_types.standart5x5, iterations=5)


'''Сохранение результата'''

Generator.SaveFromNdarray(field, "res")
# Generator.SaveFromNdarray(field, local_time)
end = time.time()
