import Generator
import blur_types
import rules

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

l, d = 10, 1
for _ in range(2):
    field = Generator.RunAutomaton(field, l, d, 250, rules.moore_neighborhood_1order)
    # l, d = d, l
    field = Generator.Blur(field, blur_type=blur_types.standart3x3, target_values=[1], iterations=20)
    # field = Generator.ReplaceCells(field, replace=[2, 3, 4, 5, 6, 7, 8, 9], to=[10])
    field = Generator.ReplaceCells(field, replace=[1, 2], to=[7, 8, 9], p=0.05)
    field = Generator.Blur(field, blur_type=blur_types.standart5x5, iterations=10)


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
