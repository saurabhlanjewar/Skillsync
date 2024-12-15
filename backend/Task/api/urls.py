from django.urls import path
from .views import TaskCreate, TaskDetail, GroupTaskList, UserTaskList

urlpatterns = [
    path("tasks/", TaskCreate.as_view()),
    path("tasks/<int:task_id>/", TaskDetail.as_view()),
    path("groups/<int:group_id>/tasks/", GroupTaskList.as_view()),
    path("users/<int:user_id>/tasks/", UserTaskList.as_view()),
    # path("groups/<int:group_id>/remove/<slug:username>/", GroupRemoveMember.as_view()),
    # path('group/<int:group_id>/discuss/', GroupDetail.as_view()),
]
