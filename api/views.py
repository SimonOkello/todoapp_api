import re
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from .serializers import TaskSerializer
from .models import Task

# Create your views here.

class TaskListView(ListAPIView):
    model =Task
    serializer_class = TaskSerializer
    queryset = Task.objects.all().order_by('-created_at')


# @api_view(['GET'])
# def taskList(request):
#     tasks = Task.objects.all().order_by('-created_at')
#     serializer = TaskSerializer(tasks, many=True)
#     return Response(serializer.data)


class TaskDetail(RetrieveAPIView):
     queryset = Task.objects.all()
     serializer_class = TaskSerializer



# @api_view(['GET'])
# def taskDetail(request, pk):
#     task = Task.objects.get(pk=pk)
#     serializer = TaskSerializer(task, many=False)
#     return Response(serializer.data)


class CreateTask(CreateAPIView):
    serializer_class = TaskSerializer



@api_view(['POST'])
def updateTask(request, pk):
    task = Task.objects.get(pk=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteTask(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return Response("Item successfully deleted")
