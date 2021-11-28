from django.urls import path

from .views import (
    TaskListView,
    TaskDetail,
    CreateTask,
    UpdateTask,
    DeleteTask
)
app_name = 'api'
urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/<str:pk>/detail/', TaskDetail.as_view(), name='task-detail'),
    path('create-task/', CreateTask.as_view(), name='create-task'),
    path('tasks/<str:pk>/update/', UpdateTask.as_view(), name='update-task'),
    path('tasks/<str:pk>/delete/', DeleteTask.as_view(), name='delete-task')
]
