from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

from .forms import ProjectForm
from .models import Project


def register_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProjectForm()

    return render(request, 'reg.html', {'form': form})


def register_student(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_login')
    else:
        form = UserCreationForm()

    return render(request, 'student_register.html', {'form': form})


def index(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {'projects': projects})
