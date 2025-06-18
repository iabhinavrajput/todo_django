from django.urls import path
from .import views

urlpatterns = [
    path('', views.api_overview, name="api_overview"),
    path('task_list_get/', views.task_list_get, name="task_list_get"),
    path('task_detail/<int:id>/', views.task_detail, name="task_detail"),
    path('task_create/', views.task_create, name="task_create"),

]