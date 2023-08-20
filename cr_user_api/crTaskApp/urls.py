from django.urls import path
from .views import taskCreate, TaskListView, TaskDetail, TaskUpdate, TaskDestroy

urlpatterns = [
    path('task-create/', taskCreate, name='task-create'),
    path('task-list/', TaskListView, name='task-list'),
    path('task-details/<int:task_id>/', TaskDetail, name='task-details'),
    path('task-update/<int:task_id>/', TaskUpdate, name='task-update'),
    path('task-delete/<int:task_id>/', TaskDestroy, name='task-delete'),

]
