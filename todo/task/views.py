from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

from django.http import HttpResponse

def index(req):
    tasks = Task.objects.all()

    form = TaskForm()

    if req.method == 'POST':
        form = TaskForm(req.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks': tasks, 'form': form}

    return render(req, 'task/list.html', context)

def updateTask(req, pk):

    task = Task.objects.get(id = pk)

    form = TaskForm(instance=task)

    if req.method == "POST":
        form = TaskForm(req.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(req, 'task/update_task.html', context)

def deleteTask(req, pk):
    item = Task.objects.get(id=pk)

    if req.method == "POST":
        item.delete()
        return redirect('/')

    context = {'item': item}

    return render(req, 'task/delete.html', context)