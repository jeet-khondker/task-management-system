from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Task

from .serializers import TaskListSerializer

# Overview of ToDo Task related API Endpoints
class TaskAPIOverview(APIView):
    """
    List of all Task related API Endpoints
    """
    def get(self, request):
        api_urls = {
            "Task List View" : "/tasks/",
            "Task Detailed View" : "/tasks/<int:pk>/",
            "Create Task View" : "/tasks/create/",
            "Update Task View" : "/tasks/update/<int:pk>/",
            "Delete Task View" : "/tasks/delete/<int:pk>/",
        }

        return Response(api_urls)

# List View of All Tasks
class TaskList(ListAPIView):
    """
    List all ToDo Task Items
    """
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer

# Task Detailed View
class TaskDetail(RetrieveAPIView):
    """
    Retrieve a particular task item instance
    """
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer