from django.db import models

from django.utils import timezone

# Task Table Model
class Task(models.Model):
    title = models.CharField(verbose_name="Task Title", max_length=150)
    description = models.TextField(verbose_name="Task Description")
    date_created = models.DateTimeField(verbose_name="Date Created", auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name="Date Updated", auto_now=True)
    due_date = models.DateField(verbose_name="Due Date", default=timezone.now().strftime("%Y-%m-%d"))
    is_completed = models.BooleanField(verbose_name="Completed Status", default=False)
    date_completed = models.DateTimeField(verbose_name="Date Completed")

    class Meta:
        db_table = "todoitems"
        ordering = ["-date_created"]

    def __str__(self):
        return self.title