from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

def index(request):
    task = Task.objects.all()
    return render(request,'main/index.html', {'title': 'Задачи', 'task': 'Купить хлеб',
                                                         'date':'17.01', 'name':'Имя'})

def about(request):
    return render(request,'main/about.html')

def new(request):
    return render(request,'main/new.html')

def exampleHTML(request):
    return render(request,'main/exampleHTML.html')
