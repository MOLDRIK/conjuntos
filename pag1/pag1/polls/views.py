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

def formulario(request):
    return render(request, 'polls/index.html')

def index(request):
    context = {}
    if request.method == 'POST':
        # Capturar los datos del formulario
        apartamento = request.POST.get('apartamento')
        nombre = request.POST.get('nombre')
        apellidos = request.POST.get('apellidos')
        capital = float(request.POST.get('capital', 0))
        correo = request.POST.get('correo')
        cartera = request.POST.get('carteras')

        # Calcular los honorarios y el total
        honorarios = capital * 0.10
        total = capital + honorarios

        # Añadir los datos calculados al contexto para mostrarlos en la plantilla
        context = {
            'apartamento': apartamento,
            'nombre': nombre,
            'apellidos': apellidos,
            'capital': capital,
            'honorarios': honorarios,
            'total': total,
            'correo': correo,
            'cartera': cartera,
        }

        # Opcional: Guardar los datos en la base de datos o realizar alguna acción
        # Aquí puedes añadir la lógica para guardar los datos en el modelo correspondiente

        # Redirigir a una página de éxito o volver a mostrar el formulario con los datos calculados
        return render(request, 'polls/index.html', context)
    return render(request, 'polls/index.html', context)