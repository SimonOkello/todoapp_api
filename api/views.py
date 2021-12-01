from django.http import request
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView
from rest_framework import permissions
from rest_framework.response import Response
from .serializers import TaskSerializer, UserSerializer
from django.contrib.auth.models import User
from .models import Task
from .permissions import isOwnerOrReadOnly

# Create your views here.


class TaskList(ListCreateAPIView):
    queryset = Task.objects.select_related('owner').all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated,]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class TaskDetail(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.select_related('owner').all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, isOwnerOrReadOnly]


# USER VIEWS

class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated,]


class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
