from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Task
from .serializers import TaskSerializer

# from django.contrib.auth.models import User


class TaskCreate(APIView):

    def post(self, request):
        serializer = TaskSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class TaskDetail(APIView):
    def get(self, request, task_id):
        if Task.objects.filter(id=task_id).exists():
            task = Task.objects.get(id=task_id)
            serializer = TaskSerializer(task)
            return Response(serializer.data, status=200)
        return Response(status=400)

    def delete(self, request, task_id):
        if Task.objects.filter(id=task_id).exists():
            task = Task.objects.get(id=task_id)
            task.delete()
            return Response(status=204)
        return Response(status=400)


class GroupTaskList(APIView):
    def get(self, request, group_id):
        if Task.objects.filter(group_name__id=group_id).exists():
            tasks = Task.objects.filter(group_name__id=group_id)
            serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data, status=200)
        return Response(status=400)


class UserTaskList(APIView):
    def get(self, request, user_id):
        if Task.objects.filter(assigned_user__id=user_id).exists():
            tasks = Task.objects.filter(assigned_user__id=user_id)
            serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data, status=200)
        return Response(status=400)
