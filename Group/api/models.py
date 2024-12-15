from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Group(models.Model):
    group_name = models.CharField(max_length=30)
    group_description = models.CharField(max_length=225)
    skill_learn = models.JSONField(blank=True, default=list)
    group_members = models.ManyToManyField(User, related_name="group_list")