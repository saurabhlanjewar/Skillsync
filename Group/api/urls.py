from django.urls import path
from .views import GroupsView, GroupDetail, GroupAddMember, GroupRemoveMember

urlpatterns = [
    path("groups/", GroupsView.as_view()),
    path("groups/<int:group_id>/", GroupDetail.as_view()),
    path("groups/<int:group_id>/add/<slug:username>/", GroupAddMember.as_view()),
    path("groups/<int:group_id>/remove/<slug:username>/", GroupRemoveMember.as_view()),
    # path('group/<int:group_id>/discuss/', GroupDetail.as_view()),
]
