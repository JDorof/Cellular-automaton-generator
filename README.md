# Cellular-automaton-generator

Процедурный генератор изображений-местностей, основанный на клеточных автоматах.

---
## Полезные ссылки:

- [Жизнь, Майнкрафт и Процедурная Генерация](https://www.youtube.com/watch?v=YtXvqJzKL70 "Видео про использование клеточных автоматов в генерации местности и тп")
- [День и ночь (клеточный автомат)](https://ru.wikipedia.org/wiki/%D0%94%D0%B5%D0%BD%D1%8C_%D0%B8_%D0%BD%D0%BE%D1%87%D1%8C_(%D0%BA%D0%BB%D0%B5%D1%82%D0%BE%D1%87%D0%BD%D1%8B%D0%B9_%D0%B0%D0%B2%D1%82%D0%BE%D0%BC%D0%B0%D1%82) "Статья в википедии")
- [Python Image Module](https://pillow.readthedocs.io/en/stable/reference/Image.html "Встроенный модуль Python для обработки изображений")
- [Размытие по Гауссу](https://ru.wikipedia.org/wiki/%D0%A0%D0%B0%D0%B7%D0%BC%D1%8B%D1%82%D0%B8%D0%B5_%D0%BF%D0%BE_%D0%93%D0%B0%D1%83%D1%81%D1%81%D1%83 "Статья в википедии")
- [Матричные фильтры обработки изображений](https://habr.com/ru/articles/142818/ "Статья на habr")
- [Нормальное распределение](https://ru.wikipedia.org/wiki/%D0%9D%D0%BE%D1%80%D0%BC%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%B5_%D1%80%D0%B0%D1%81%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5 "Статья в википедии")
- [Отображение структуры фалов](https://bobbyhadz.com/blog/markdown-display-directory-and-file-structure "Статья")
- [Логирование в Python: руководство разработчика](https://habr.com/ru/companies/wunderfund/articles/683880/ "Статья на habr")

---
## Возможные наработки в будущем

- Добавить шумы перлина и другие типы генерации
- Сделать генератор templates
- Генератор градиентов (левый, правый) (словарик индекс:цвет)
- Разобраться с матрицей контраста (при варианте, когда вокруг 10-ки стоят 1 результат получается = 82)
- Сделать отлов ошибок и Warnings (матрицы окрестностей должны быть int32, не bool)

<!-- (np.logical_or(Generator.NeighborhoodClass.cross,  Generator.NeighborhoodClass.horizontal).astype("int32")) -->