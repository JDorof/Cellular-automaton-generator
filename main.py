import rules
import blur_types
import Generator

from os import mkdir
import time
import logging

start = time.time()
local_time = time.asctime().replace(':', '_')[4:19]
mkdir(path=f'results/{local_time}')
logging.basicConfig(level=logging.INFO, filename=f'results/{local_time}/log.log', filemode="w")

'''Генерация'''



field = Generator.InitializeField([10, 1], (rules.height, rules.width))

# field = Generator.InitializeField([10, 1], (rules.height, rules.width))
# field = Generator.RunAutomaton(field, 10, 1, 200, rules.moore_neighborhood_1order)
# field = Generator.ReplaceCells(field, replace=[1], to=[3], p=0.5)
# field = Generator.RunAutomaton(field, 3, 1, 25, rules.moore_neighborhood_1order)
# field = Generator.ReplaceCells(field, replace=[10], to=[8], p=0.5)
# field = Generator.RunAutomaton(field, 8, 10, 25, rules.moore_neighborhood_1order)
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


field = Generator.InitializeField([10, 1], (rules.height, rules.width))
for _ in range(2):
    field = Generator.RunAutomaton(field, 10, 1, {3, 6, 7, 8}, {3, 4, 6, 7, 8}, 250, rules.moore_neighborhood_1order)
    field = Generator.Blur(field, blur_type=blur_types.standart3x3, target_values=[1], iterations=20)
    field = Generator.ReplaceCells(field, replace=[2, 3, 4, 5, 6, 7, 8, 9], to=[10])
    field = Generator.ReplaceCells(field, replace=[1, 2], to=[7, 8, 9], p=0.05)
    field = Generator.Blur(field, blur_type=blur_types.standart5x5, iterations=10)
field = Generator.ReplaceCells(field, replace=[10], to=[1, 2], p=1)
field = Generator.Blur(field, blur_type=blur_types.standart5x5, iterations=5)


'''Сохранение результата'''

Generator.SaveFromNdarray(field, local_time)
end = time.time()
