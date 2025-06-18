from django.urls import path
from . import views

urlpatterns =[
    path('', views.task_list, name='task_list'),
    path('complete/<int:task_id>/', views.complete_task, name='complete_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('uncheck/<int:task_id>/', views.unceck_task, name='uncheck_task'),
    path('delete_all/', views.delete_all_tasks, name='delete_all_tasks'),
]