from django.shortcuts import render

# Create your views here.


def todoList(request):
    context = {}
    return render(request, 'frontend/task-list.html', context)
