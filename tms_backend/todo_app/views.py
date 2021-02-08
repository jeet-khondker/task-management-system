from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Task

from .serializers import TaskSerializer

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