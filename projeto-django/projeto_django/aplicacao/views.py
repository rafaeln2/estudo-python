from django.shortcuts import render

from .models import TodoItem

def home(request):
    return render(request, 'aplicacao/home.html')

def todos(request):
    return render(request, 'aplicacao/todos.html', {'todos': TodoItem.objects.all()})