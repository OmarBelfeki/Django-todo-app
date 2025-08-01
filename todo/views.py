from django.shortcuts import render, redirect
from .models import Task


def index(request):
    tasks = Task.objects.all()
    if request.method == "POST":
        title = request.POST["title"]
        Task.objects.create(title=title)
        return redirect("/")
    return render(request, "todo/index.html", {"tasks": tasks})


def delete_task(request, task_id):
    Task.objects.get(id=task_id).delete()
    return redirect("/")


def toggle_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect("/")
