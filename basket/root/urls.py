from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('/index', views.root, name='root'),
    # ex: /polls/5/
]