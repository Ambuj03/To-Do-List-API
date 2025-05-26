from django.shortcuts import render
from .serializers import taskSerializer
from rest_framework import generics, authentication, permissions
from .models import Tasks


class ListTasks(generics.ListCreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = taskSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]  

    def get_queryset(self):
        return Tasks.objects.filter(user = self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)


class UpdateTasks(generics.UpdateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = taskSerializer

    def get_queryset(self):
        return Tasks.objects.filter(user = self.request.user)
    
    def perform_update(self, serializer):
        serializer.save(user = self.request.user)


class DeleteTasks(generics.DestroyAPIView):
    queryset = Tasks.objects.all()
    serializer_class = taskSerializer

    def get_queryset(self):
        return Tasks.objects.filter(user = self.request.user)
    
    def perform_destroy(self, serializer):
        serializer.save(user = self.request.user)

