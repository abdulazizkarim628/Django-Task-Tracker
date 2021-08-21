from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone


def index(request):
    return render(request, 'index.html', context={'tasks': Task.objects.all()[::-1]})


def tasksmanager(request):
    tasks = Task.objects.all()[::-1]
    error_message = ''
    for task in tasks:
        if task.expiry_date <= timezone.now():
            task.delete()
            return redirect('/tasksmanager/')
        if task.expiry_date - task.date_created <= timezone.timedelta(days=3):
            error_message = f'Your {task.title} will expire soon..'
    return render(request, 'tasksmanager.html',
                  context={'tasks': tasks, 'error_message': error_message})


@csrf_exempt
def add_task(request):
    task = Task()
    task.title = request.GET['title']
    task.description = request.GET['description']
    task.save()
    return redirect('/tasksmanager/')


@csrf_exempt
def delete_task(request, pk):
    task = Task(id=pk)
    task.delete()
    return redirect('/tasksmanager/')


def task_detail(request, pk):
    task = get_object_or_404(Task, id=pk)
    error_message = ''
    if task.expiry_date - task.date_created <= timezone.timedelta(days=3):
        error_message = f'Your "{task.title}" task will expire soon..'
    return render(request, 'task_detail.html', context={'task': task, 'error_message': error_message})


def update_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    return render(request, 'task_update.html',
                  context={'task': task})


@csrf_exempt
def proceed(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.title = request.GET['title']
    task.description = request.GET['description']
    task.save()
    msg = 'Your task has been updated successfully!'

    return render(request, 'task_detail.html',context={'task': task, 'msg': msg})


def search(request):
    q = request.GET['q']
    query = str(q)
    unwanted = '  1234567890!"£$%^&*()_+}{~:?><|\,.;#][=-@'
    typos = ''
    for item in unwanted:
        if item in q:
            typos += item
            query = query.replace(item, '')
    tasks = Task.objects.all().filter(title__icontains=query)
    return render(request, 'search.html', context={'tasks': tasks, 'q': query, 'typos': typos})