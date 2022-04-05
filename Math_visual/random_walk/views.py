from django.shortcuts import render
from django.http import HttpResponse

def start_page(request):
    """Стартовая страница"""
    return render(request, 'startpage.html')

