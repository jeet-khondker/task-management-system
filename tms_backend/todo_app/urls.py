# URL Patterns Listing
# Application : ToDo Task

from django.urls import path

from .views import TaskAPIOverview, TaskList, TaskDetail, CreateTask, UpdateTask

urlpatterns = [
    path('', TaskAPIOverview.as_view()),
    path("tasks/", TaskList.as_view()),
    path("tasks/<int:pk>/", TaskDetail.as_view()),
    path("tasks/create/", CreateTask.as_view()),
    path("tasks/update/<int:pk>/", UpdateTask.as_view()),
]
