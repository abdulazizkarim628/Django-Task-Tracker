from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('tasksmanager/', views.tasksmanager, name='tasksmanager'),
    path('add_task/', views.add_task, name='add_task'),
    path('<int:pk>/delete_task/', views.delete_task, name='delete_task'),
    path('<int:pk>/', views.task_detail, name='task_detail'),
    path('<int:pk>/task_update/', views.update_task, name='task_update'),
    path('<int:pk>/task_update/proceed/', views.proceed, name='proceed'),
    path('search/', views.search, name='search'),
]
