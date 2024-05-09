#views.py

#imports
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from .models import Task, Profile
from .forms import ProfileForm
from .forms import TaskForm

@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user, 'profile': request.user.profile})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'edit_profile.html', {'form': form})
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. You can now log in!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
def task_list(request):
    # Handling the form submission for adding new tasks
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()

    # Categorizing tasks based on importance and urgency
    tasks = Task.objects.all()
    do_now = tasks.filter(important=True, urgent=True)
    schedule = tasks.filter(important=True, urgent=False)
    delegate = tasks.filter(important=False, urgent=True)
    limit = tasks.filter(important=False, urgent=False)

    context = {
        'form': form,
        'do_now': do_now,
        'schedule': schedule,
        'delegate': delegate,
        'limit': limit,
    }
    return render(request, 'taskMgmt/task_list.html', context)
''' old task list
def task_list(request):
    tasks = Task.objects.all()

    do_now = tasks.filter(important=True, urgent=True)
    schedule = tasks.filter(important=True, urgent=False)
    delegate = tasks.filter(important=False, urgent=True)
    limit = tasks.filter(important=False, urgent=False)

    context = {
        'do_now': do_now,
        'schedule': schedule,
        'delegate': delegate,
        'limit': limit,
    }
    return render(request, 'taskMgmt/task_list.html', context)
'''

'''    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')

    return render(request, 'taskMgmt/task_list.html', {'tasks': tasks, 'form': form})'''

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'taskMgmt/add_task.html', {'form': form})

def mark_complete(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')


def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect('task_list')


def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'taskMgmt/task_detail.html', {'task': task})

def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)

    return render(request, 'taskMgmt/edit_task.html', {'form': form})