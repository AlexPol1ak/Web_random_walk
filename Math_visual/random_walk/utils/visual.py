from .random_walk import RandomPoints

import os
import shutil

import matplotlib.pyplot as plt

import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly import offline

# static_path = '../static/result_pic'


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


def dual2d(nums1=5000):
    """Визуализация двух блужданий"""
    obj1 = RandomPoints(nums1)
    obj2 = RandomPoints(nums1)
    obj1.random_walk()
    obj2.random_walk()

    x1 = obj1.list_value('x')
    y1 = obj1.list_value('y')
    x2 = obj2.list_value('x')
    y2 = obj2.list_value('y')

    plt.style.use('classic')
    fig, ax = plt.subplots(dpi=90)
    color1 = range(nums1)
    color2 = range(nums1)

    # Первое блуждание.
    ax.scatter(x1, y1, c=color1, cmap=plt.cm.Blues, edgecolors='none', s=10)
    ax.scatter(0, 0, c='blue', edgecolors='none', s=300)
    ax.scatter(x1[-1], y1[-1], c='blue', edgecolors='none', s=200)

    # Второе блуждание.
    ax.scatter(x2, y2, c=color2, cmap=plt.cm.Greens, edgecolors='none', s=10)
    ax.scatter(0, 0, c='green', edgecolors='none', s=300)
    ax.scatter(x2[-1], y2[-1], c='green', edgecolors='none', s=200)

    # Проверка и отображение пересечений двух блужданий.
    intersection_x, intersection_y = [], []
    i = 0
    while i < len(x1):
        if x1[i] in x2 and y1[i] in y2:
            intersection_x.append(x1[i])
            intersection_y.append(y1[i])
        i += 1
    if len(intersection_x) != 0:
        ax.scatter(intersection_x, intersection_y, c='yellow', edgecolors='none', s=10, alpha=0.1)

    pic_name = 'rw_dual2D.png'
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

def visual3D(nums = 5000):
    obj = RandomPoints(nums)
    obj.random_walk()

    x = obj.list_value('x')
    y = obj.list_value('y')
    z = obj.list_value('z')

    fig = make_subplots(
        rows=2, cols=2,
        specs=[[None, None],
               [{"type": "scene"}, {"type": "scatter3d"}]], start_cell='bottom-left')
    fig.add_trace(go.Scatter3d(x=x, y=y,
                               z=z, mode='lines'),
                  row=2, col=2)

    fig.update_layout(autosize=True, width=1500, height=1500, showlegend=False, template="plotly_dark", )
    name = 'rw3Dv.html'

    # paper_bgcolor="darkgray"
    offline.plot({'data': fig}, filename=name,)




