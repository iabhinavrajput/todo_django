from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

def task_list(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title) 
        return redirect('task_list')
    tasks = Task.objects.all()
    return render(request, 'todo/task_list.html', {'tasks':tasks})


def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.save()
    return redirect('task_list')


def delete_task(request, task_id):
    task = get_object_or_404(Task, id = task_id)
    task.delete()
    return redirect('task_list')


def edit_task(request, task_id):
    task = get_object_or_404(Task,id=task_id)
    if request.method =='POST':
        new_title = request.POST.get('title')
        if new_title:
            task.title = new_title
            task.save()
            return redirect('task_list')
    return render(request, 'todo/edit_task.html', {'task':task})


def unceck_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = False
    task.save()
    return redirect('task_list')


def delete_all_tasks(reuest):
    Task.objects.all().delete()
    return redirect('task_list')


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'List' : '/task_list/',
        'Details' : '/task_details/<int:id>/',
        'Create': '/task-create/',
        'Update': '/task-update/<int:id>/',
        'Delete': '/task-delete/<int:id>/',
    }
    return Response(api_urls)


@api_view(["GET"])
def task_list_get(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def task_detail(request,id):
    try:
        task = Task.objects.get(id=id)
    except Task.DoesNotExist:
        return Response({'error' : 'Task no found'}, status=404)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)

@api_view(['POSt'])
def task_create(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['PUT'])
def task_update(request, id):
    task = get_object_or_404(Task, id=id)
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def task_delete(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return Response({"message" : "Task deleted successfully"}, status=200)