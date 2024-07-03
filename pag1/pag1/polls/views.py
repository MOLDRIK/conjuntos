from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Choice, Question

# views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Bienvenido a la pagina principal")
