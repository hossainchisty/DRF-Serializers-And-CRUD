from django.urls import path
from . import views

urlpatterns = [
    
    # http://127.0.0.1:8000/api/task-list

    path('task-list/', views.taskList, name='task-list'),
    path('task-create/', views.taskCreate, name='task-create'),
    
    path('task-update/<str:pk>/', views.taskUpdate, name='task-update'),
    path('task-delete/<str:pk>/', views.taskDelete, name='task-delete'),
    path('task-details/<str:pk>/', views.taskDetail, name='task-detail'),

]