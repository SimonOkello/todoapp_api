from django.urls import path

from .views import (
    taskList,
    taskDetail,
    createTask,
    updateTask,
    deleteTask
)
app_name = 'api'
urlpatterns = [
    path('tasks/', taskList, name='task-list'),
    path('tasks/<str:pk>/detail/', taskDetail, name='task-detail'),
    path('create-task/', createTask, name='create-task'),
    path('tasks/<str:pk>/update/', updateTask, name='update-task'),
    path('tasks/<str:pk>/delete/', deleteTask, name='delete-task')
]
