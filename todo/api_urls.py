from django.urls import path
from .import views

urlpatterns = [
    path('', views.api_overview, name="api_overview"),
    path('task_list/', views.task_list, name="task_list"),
]