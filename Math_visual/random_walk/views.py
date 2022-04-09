from django.shortcuts import render
from django.http import HttpResponse
from .forms import AmountPoints
from .utils.visual import visual2D


def start_page(request):
    """Стартовая страница"""
    return render(request, 'startpage.html')

def rw2d(request):
    """Отображение случайного блуждения в 2d"""

    us2d = AmountPoints()
    context = {'w2d': us2d}
    if request.method == 'POST':
        points = request.POST.get('points')
        pic_name = visual2D(int(points))
        context['points'] = points

    return render(request, 'rw2d.html', context)

def rwdual2d(request):
    """Отображение пересечения двух блужданий в 2d"""

    return render(request, 'rwdual2d.html', )

