from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_page),
    path('2d/', views.rw2d),
    path('dual2d/',views.rwdual2d),
    path('3d/',views.rw3d)
]
