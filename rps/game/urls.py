from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('load/', views.load_game, name='load'),
    path('play/', views.play, name='play'),
]
