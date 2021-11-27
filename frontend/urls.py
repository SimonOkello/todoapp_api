from django.urls import path

from .views import (
    todoList,
    # taskDetail,
    # createTask,
    # updateTask,
    # deleteTask
)
app_name = 'frontend'
urlpatterns = [
    path('', todoList, name='todo-list'),
    # path('tasks/<str:pk>/detail/', taskDetail, name='task-detail'),
    # path('create-task/', createTask, name='create-task'),
    # path('tasks/<str:pk>/update/', updateTask, name='update-task'),
    # path('tasks/<str:pk>/delete/', deleteTask, name='delete-task')
]
