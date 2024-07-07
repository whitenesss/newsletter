from django.shortcuts import render
from django.views.generic import ListView

from logi.models import Logi


# Create your views here.
class LogiListView(ListView):
    """
    Контроллер отвечающий за отображение списка попыток рассылок
    """
    model = Logi