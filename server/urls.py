from django.urls import path
from . import views

urlpatterns = [
    path('users/create/', views.CreateUserView.as_view(), name='create-user'),
    path('tasks/create/', views.CreateTaskView.as_view(), name='create-task'),
    path('tasks/<int:task_id>/assign/', views.assign_task, name='assign-task'),
    path('users/<int:user_id>/tasks/', views.get_tasks_by_user, name='user-tasks'),
]
