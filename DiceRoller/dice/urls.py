# dice/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('roll/', views.roll_dice, name='roll_dice'),
]
