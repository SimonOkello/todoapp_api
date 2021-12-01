from django.urls import path

from .views import (
    TaskList,
    TaskDetail,
    UserList,
    UserDetail
)
app_name = 'api'
urlpatterns = [
    path('tasks/', TaskList.as_view(), name='task-list'),
    path('tasks/<str:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<str:pk>/', UserDetail.as_view(), name='user-detail'),
]
