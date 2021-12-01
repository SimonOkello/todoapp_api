from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
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
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
