from django.contrib import admin

from .models import Task

# Task Admin
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "date_created", "date_updated", "due_date", "is_completed", "date_completed")

admin.site.register(Task, TaskAdmin)