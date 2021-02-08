# URL Patterns Listing
# Application : ToDo Task

from django.urls import path

from .views import TaskAPIOverview

urlpatterns = [
    path('', TaskAPIOverview.as_view()),
]
