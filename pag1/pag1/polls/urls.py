# polls/urls.py
from django.urls import path
from . import views
from django.http import HttpResponse

def index(request):
    return HttpResponse("Bienvenido a la pagina principal")


urlpatterns = [
    path('', views.index, name='index'),
]
