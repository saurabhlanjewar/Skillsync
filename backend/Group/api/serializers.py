from rest_framework import serializers
from .models import Group
from Task.api.serializers import TaskSerializer


class GroupSerializer(serializers.ModelSerializer):
    task_list = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = "__all__"
