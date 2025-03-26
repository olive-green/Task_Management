from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Task, User
from .serializers import TaskSerializer, UserSerializer

class CreateTaskView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['POST'])
def assign_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    user_ids = request.data.get("user_ids", [])
    users = User.objects.filter(id__in=user_ids)
    task.assigned_users.set(users)
    task.save()
    return Response({"message": "Task assigned successfully."})

@api_view(['GET'])
def get_tasks_by_user(request, user_id):
    user = User.objects.get(pk=user_id)
    tasks = user.tasks.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)
