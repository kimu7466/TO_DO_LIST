from django.shortcuts import render, redirect

# Create your views here.
def main_view(request):



    return render(request , "master/main.html")

# from django.shortcuts import render, redirect
from .models import Tasks
from .forms import TaskForm

def task_list(request):
    tasks = Tasks.objects.all()
    return render(request, 'master/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'master/add_task.html', {'form': form})
