from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.task_list, name='task-list'),

    path('toggle-status/<int:pk>/', views.toggle_status, name='toggle-status')
]