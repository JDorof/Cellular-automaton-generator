import Generator
import blur_types
import rules

# import random
# import numpy as np
from PIL import Image
import time

# TODO
'''По окончании генератора сохранять код исполняемого файла, сид и тп в отдельный файл Лога, чтобы можно было повторить'''
'''Вынести правила B*/S* в параметр функции Generate и убрать из rules'''
'''Сделать маштабируемый блюр и расширение спрайта'''
'''Сделать отдельный фалй-интерфейс, в котором прописывать весь код'''
'''Распихать файлы по папкам для удобства'''
'''Логирование результата'''
'''Генератор градиентов (левый, правый) (словарик индекс:цвет)'''

'''Подготовка'''

start = time.time()


print(f'{rules.seed = }')

im = Image.new('RGB', (rules.width, rules.height))
# im2 = Image.new('RGB', (rules.width + 2, rules.height + 2))
# im3 = Image.new('RGB', (rules.width, rules.height))

field = Generator.InitializeField(rules.chances, (rules.height, rules.width))


'''Генерация'''

field = Generator.RunAutomaton(field, 8, 3, 3200, rules.moore_neighborhood_1order)


# for i in range(5):
#     field = Generator.Blur(field, blur_type=blur_types.cross)


field = Generator.Shuffle_field(field, [1], {3}, 5)
field = Generator.RunAutomaton(field, 1, 3, 200, rules.moore_neighborhood_1order)

# field = Generator.Shuffle_field(field, [4], {1, 3}, 2)
# field = Generator.RunAutomaton(field, 4, 3, 250, rules.moore_neighborhood_1order)

field = Generator.Shuffle_field(field, [10], {8}, 4)
field = Generator.RunAutomaton(field, 10, 8, 100, rules.moore_neighborhood_1order)

for i in range(10):
    field = Generator.Blur(field, blur_type=blur_types.cross)



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
