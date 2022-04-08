import matplotlib.pyplot as plt
import os
import shutil
from random_walk import RandomPoints3D

static_path = '../static/result_pic'



def visual2D(dst_pic = static_path, nums=5000):
    # dst_pic- Путь, куда сохраняет картинку. nums- количество отрисованных точек,
    """Визуализация случайного блуждания в 2D"""

    obj = RandomPoints3D(nums)
    obj.random_walk()
    x = obj.list_value('x')
    y = obj.list_value('y')

    plt.style.use('classic')
    fig, ax = plt.subplots( dpi=90)
    point_number = range(nums)
    ax.scatter(x, y, c=point_number, cmap=plt.cm.Blues, edgecolors='none', s=5)
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(x[-1], y[-1], c='red', edgecolors='none', s=100)
    pic_name = 'rw_visual2D.png'
    plt.savefig(pic_name, bbox_inches='tight')

    # Инструкция позволяющая перезаписать отрисованную картинку, если она была сохранена ранее
    if dst_pic:
        try:
            os.remove(dst_pic + f'/{pic_name}')
        except FileNotFoundError:
            shutil.move(pic_name, dst_pic)
        else:
            shutil.move(pic_name, dst_pic)


#visual2D()