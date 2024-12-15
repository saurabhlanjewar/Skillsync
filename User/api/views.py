from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
from django.contrib.auth.models import User
from .serializers import UserSerializers

from rest_framework_simplejwt.tokens import RefreshToken


class UserProfile(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializers(users, many=True)
        return Response(serializer.data, status=200)


# login
class Login(APIView):
    def post(self, request):
        username = request.data["username"]
        password = request.data["password"]
        user = authenticate(username=username, password=password)
        # user = None
        if user is not None:
            refresh = RefreshToken.for_user(user)
            token = {"refresh": str(refresh), "access": str(refresh.access_token)}
            return Response(token, status=200)
        return Response({"error": "username or password is incorrect"}, status=400)


# register


class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            # token = Token.objects.create(user=account).key
            refresh = RefreshToken.for_user(account)
            token = {"refresh": str(refresh), "access": str(refresh.access_token)}
            return Response({"data": serializer.data, "token": token})
        return Response(status=400)
