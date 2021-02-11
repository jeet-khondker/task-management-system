# URL Patterns Listing
# Application : ToDo Task

from django.urls import path

from .views import TaskAPIOverview, TaskList

urlpatterns = [
    path('', TaskAPIOverview.as_view()),
    path("tasks/", TaskList.as_view()),
]
