from rest_framework.serializers import ModelSerializer

from .models import Task

# ToDo Task List Serializer
class TaskListSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ["title", "description", "date_created", "date_updated", "due_date", "is_completed", "date_completed"]

# ToDo Task Item Detail Serializer
class TaskDetailSerializer(ModelSerializer):

    class Meta:
        model = Task
        fields = ["id", "title", "description", "date_created", "date_updated", "due_date", "is_completed", "date_completed"]

# Create ToDo Task Serializer
class TaskCreateSerializer(ModelSerializer):

    class Meta:
        model = Task
        fields = ["title", "description", "date_created", "due_date"]

# Update ToDo Task Serializer
class TaskUpdateSerializer(ModelSerializer):

    class Meta:
        model = Task
        fields = ["id", "title", "description", "date_updated", "due_date"]

# Delete ToDO Task Serializer
class TaskDeleteSerializer(ModelSerializer):

    class Meta:
        model = Task
        fields = ["id", "title", "description", "date_created", "date_updated", "due_date", "is_completed", "date_completed"]