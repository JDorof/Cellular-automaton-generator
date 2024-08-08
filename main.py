import Generator
import blur_types
import rules
from random import randint, choice
import numpy as np
from PIL import Image
import time

start = time.time()

# TODO
'''По окончании генератора сохранять код исполняемого файла, сид и тп в отдельный файл Лога, чтобы можно было повторить'''
'''Вынести правила B*/S* в параметр функции Generate и убрать из rules'''
'''Генератор через сиды, а не randint'''
'''Сделать маштабируемый блюр и расширение спрайта'''
'''Сделать настройку на симметричность и в блюре и в генераторе'''
'''Заранее выдать оценки по времени (время - этот компьютер, а в принципе сделать коэффициентом)'''
'''Сделать отдельный фалй-интерфейс, в котором прописывать весь код'''
'''Распихать файлы по папкам для удобства'''
'''Логирование результата'''
'''Генератор градиентов (левый, правый) (словарик индекс:цвет)'''
# from random import choice TODO


# Связи с другими файлами

'''Подготовка'''

im = Image.new('RGB', (rules.width, rules.height))
# im2 = Image.new('RGB', (rules.width + 2, rules.height + 2))
# im3 = Image.new('RGB', (rules.width, rules.height))

field = Generator.InitializeField(rules.chances, (rules.height, rules.width))

'''Генерация'''


field = Generator.RunAutomaton(
    field, 10, 1, 200, rules.moore_neighborhood_1order, boundary="wrap"
)


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
