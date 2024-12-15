from django.shortcuts import render


from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Group
from .serializers import GroupSerializer
from django.contrib.auth.models import User


class GroupsView(APIView):

    def get(self, request):
        groups = Group.objects.all()
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = GroupSerializer(request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class GroupDetail(APIView):

    def get(self, request, group_id):
        if Group.objects.filter(id=group_id).exists():
            group = Group.objects.get(id=group_id)
            serializer = GroupSerializer(group)
            return Response(serializer.data, status=200)
        return Response(status=400)


class GroupAddMember(APIView):
    def get(self, request, group_id, username):
        try:
            group = Group.objects.get(id=group_id)
            user = User.objects.get(username=username)
            group.group_members.add(user)
            serializer = GroupSerializer(group)
            return Response(serializer.data, status=200)
        except:
            return Response(status=400)


class GroupRemoveMember(APIView):
    def get(self, request, group_id, username):
        try:
            group = Group.objects.get(id=group_id)
            user = User.objects.get(username=username)
            group.group_members.remove(user)
            serializer = GroupSerializer(group)
            return Response(serializer.data, status=200)
        except:
            return Response(status=400)
