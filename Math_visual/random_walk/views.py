from django.shortcuts import render
from django.http import HttpResponse

def start_page(request):
    """Стартовая страница"""
    return render(request, 'startpage.html')

def rw2d(request):
    """Отображение случайного блуждения в 2d"""
    return render(request, 'rw2d.html')

