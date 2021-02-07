from rest_framework.serializers import ModelSerializer

from .models import Task

# ToDo Task Serializer
class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ["title", "description", "date_created", "date_updated", "due_date", "is_completed", "date_completed"]