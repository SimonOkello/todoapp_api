from django.urls import path

from .views import (
    TaskListView,
    TaskDetail,
    CreateTask,
    updateTask,
    deleteTask
)
app_name = 'api'
urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/<str:pk>/detail/', TaskDetail.as_view(), name='task-detail'),
    path('create-task/', CreateTask.as_view(), name='create-task'),
    path('tasks/<str:pk>/update/', updateTask, name='update-task'),
    path('tasks/<str:pk>/delete/', deleteTask, name='delete-task')
]
