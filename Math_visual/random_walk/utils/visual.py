import matplotlib.pyplot as plt
import os
import shutil
from .random_walk import RandomPoints


#static_path = '../static/result_pic'



def visual2D(nums=5000):
    # nums- количество отрисованных точек,
    """Визуализация случайного блуждания в 2D"""

    obj = RandomPoints(nums)
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
    # Cохранение картинки
    plt.savefig(pic_name, bbox_inches='tight')

    # Инструкция позволяющая переместить в static/result_pic
    # и перезаписать отрисованную картинку, если она была сохранена ранее
    try:
        shutil.move(pic_name, 'random_walk/static/result_pic')
    except shutil.Error:
        os.remove('random_walk/static/result_pic' + f'/{pic_name}')
        shutil.move(pic_name, 'random_walk/static/result_pic')

    return pic_name


def dual2d(nums1 = 5000, nums2 = 5000):
    """Визуализация двух блужданий"""
    pass
