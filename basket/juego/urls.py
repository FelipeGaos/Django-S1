from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('/index', views.index, name='index'),
    path('/jugadores', views.list_jugadores, name='list_jugadores'),
    # ex: /polls/5/
]