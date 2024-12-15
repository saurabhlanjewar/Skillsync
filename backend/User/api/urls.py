from django.urls import path
from .views import UserProfile, RegisterUser, Login

urlpatterns = [
    path("users/", UserProfile.as_view()),
    path("login/", Login.as_view()),
    path("register/", RegisterUser.as_view()),
]
