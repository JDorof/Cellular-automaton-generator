import Generator
import blur_types
import rules

from PIL import Image
import logging
import time



# TODO

'''Добавить шумы перлина и другие типы генерации'''

'''Добавить в генератор функцию шума перлина'''
'''Добавить сложение, вычитание и тп полей + балансировку (чтобы диапозон чисел оставался изначальным)'''

'''Вынести правила B*/S* в параметр функции Generate и убрать из rules'''
'''Сделать отдельный фалй-интерфейс, в котором прописывать весь код'''

'''Сделать полностью случайную генерацию, чтобы можно было просто так генерировать'''

'''По окончании генератора сохранять код исполняемого файла, сид и тп в отдельный файл Лога, чтобы можно было повторить'''
'''Распихать файлы по папкам для удобства'''
'''Логирование результата'''

'''Генератор градиентов (левый, правый) (словарик индекс:цвет)'''


'''Подготовка'''


local_time = time.ctime()
local_time = time.time()
local_time = time.strftime()

# logging.basicConfig(level=logging.INFO, filename=f'results/py_log.log', filemode="w")
logging.basicConfig(level=logging.INFO, filename=f'results/{local_time}.log', filemode="w")
logging.debug("A DEBUG Message")
logging.info("An INFO")
logging.warning("A WARNING")
logging.error("An ERROR")
logging.critical("A message of CRITICAL severity")

start = time.time()
print(f'{rules.seed = }')

im = Image.new('RGB', (rules.width, rules.height))
# im2 = Image.new('RGB', (rules.width + 2, rules.height + 2))
# im3 = Image.new('RGB', (rules.width, rules.height))

field = Generator.InitializeField([10, 1], (rules.height, rules.width))


'''Генерация'''


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


# field = Generator.InitializeField([10, 1], (rules.height, rules.width))
# for _ in range(2):
#     field = Generator.RunAutomaton(field, 10, 1, 250, rules.moore_neighborhood_1order)
#     field = Generator.Blur(field, blur_type=blur_types.standart3x3, target_values=[1], iterations=20)
#     # field = Generator.ReplaceCells(field, replace=[2, 3, 4, 5, 6, 7, 8, 9], to=[10])
#     field = Generator.ReplaceCells(field, replace=[1, 2], to=[7, 8, 9], p=0.05)
#     field = Generator.Blur(field, blur_type=blur_types.standart5x5, iterations=10)
# field = Generator.ReplaceCells(field, replace=[10], to=[1, 2], p=1)
# field = Generator.Blur(field, blur_type=blur_types.standart5x5, iterations=5)


'''Сохранение результата и вывод кол-ва каждого типа клеток'''


result = list(field.reshape(rules.height*rules.width))

for cell_type in range(1, 11):
    print(f'type {cell_type} = {result.count(cell_type)}')

for i in range(rules.width * rules.height):
    result[i] = rules.gradient[result[i] - 1]

im.putdata(result)
im.save(f'results/picture.png')

end = time.time()
print(end - start)
