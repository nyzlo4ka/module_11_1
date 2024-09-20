from PIL import Image, ImageFilter, ImageOps

"""
После изучения документации к Pillow, я обнаружила большой выбор возможностей для работы с графикой в Python.
Pillow значительно упроcтила мне работу, предоставляя широкий спектр инструментов для обработки изображений,
включая фильтрацию, трансформацию, применение эффектов и конвертацию форматов.
Это очень полезно для работы с графическими данными и созданием визуального контента.
"""

# Загрузка и показ изображения
image = Image.open('honda.jpg')
image.show()

# Изменение размера изображения
resized_image = image.resize((128, 128))
resized_image.show()

# Применение фильтра размытия
blur_image = image.filter(ImageFilter.BLUR)
blur_image.show()

# Отражение изображения
mirror_image = ImageOps.mirror(image)
mirror_image.show()

# Конвертация в конгревное тиснение и сохранение в новый формат
emboss_image = image.filter(ImageFilter.EMBOSS)
emboss_image.save('honda_new.png')


"""
После изучения документации к matplotlib, я обнаружила большой выбор возможностей для визуализации данных,
включая создание различных типов графиков, такие как линейные, столбчатые, гистограммы, диаграммы рассеяния и т.д. 
Одной из основных возможностей matplotlib является создание простых и настраиваемых графиков с помощью различных 
типов линий, маркеров, цветов, так же добавлять заголовки, подписи осей, чтобы сделать их более информативными.
Есть еще возможность создавать анимации и интерактивные графики с помощью функции animate() и интерфейса matplotlib.
С помощью этой библиотеки я могу создавать наглядные и информативные графики, которые помогут мне лучше понять данные
и принять обоснованные решения.
"""

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Создание столбчатой диаграммы
x = ['A', 'B', 'C', 'D']
y = [10, 20, 30, 40]
plt.bar(x, y)
plt.title('Столбчатая диаграмма')
plt.xlabel('Категории')
plt.ylabel('Значения')
plt.show()

# Создание гистограммы
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
plt.hist(data, bins=range(1, 6))
plt.title('Гистограмма')
plt.xlabel('Значения')
plt.ylabel('Частота')
plt.show()

# Создание диаграммы рассеяния
rg = np.random.Generator(np.random.PCG64(4))
data = rg.uniform(-1, 1, (30, 2))
col = np.arctan2(data[:, 1], data[:, 0])
size = 100 * np.sum(data ** 2, axis=1)
plt.scatter(data[:, 0], data[:, 1], marker='o', s=size, c=col)
plt.show()

# Создание анимированного графика
fig, ax = plt.subplots()


def animate(frame):
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x + frame / 10)
    ax.clear()
    ax.plot(x, y)
    ax.set_xlim(0, 2 * np.pi)
    ax.set_ylim(-1.5, 1.5)


ani = FuncAnimation(fig, animate, frames=range(100), interval=20)
plt.show()
