from django.db import models
# from .models import Task


# Create your models here.
class Team(models.Model):
    team_name = models.CharField(max_length=100)
    team_leader = models.CharField(max_length=100)
    members = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(null=True, blank=True)
    team_status = models.BooleanField(default=True)
    # assigned_tasks = models.ForeignKey(Task, )


    def __str__(self):
        return self.team_name

class Task(models.Model):
    task_name = models.CharField(max_length=100)
    assigned_to = models.ForeignKey(Team, related_name='teams', on_delete=models.CASCADE)
    due_date = models.DateTimeField()
    task_status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Completed', 'Completed')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task_name