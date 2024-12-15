from django.db import models

# Create your models here.
from django.db import models
from Group.api.models import Group
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    task_name = models.CharField(max_length=30)
    task_description = models.CharField(max_length=225)
    skill_used = models.JSONField(blank=True, default=list)
    deadline = models.IntegerField(default=1)
    available_all = models.BooleanField(default=False)
    group_name = models.ManyToManyField(Group, related_name="tasks_list", blank=True)
    assigned_user = models.ManyToManyField(User, related_name="todo", blank=True)