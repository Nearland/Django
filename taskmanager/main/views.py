from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    taskss = Task.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': taskss})


def about(request):
    return render(request, 'main/about.html')


def tasks(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Неверное заполнение'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/tasks.html', context)
