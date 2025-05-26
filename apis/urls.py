from django.urls import path,include
from .views import ListTasks,UpdateTasks,DeleteTasks

urlpatterns = [
    path('tasks/', ListTasks.as_view()),
    path('tasks/update/<int:pk>', UpdateTasks.as_view()),
    path('tasks/delete/<int:pk>', DeleteTasks.as_view()),
]