from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_page, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("profile/<str:pk>", views.user_profile, name="user-profile"),
    path("register/", views.register_user, name="register"),
    path("", views.home, name="home"),
    path("room/<str:pk>", views.room, name="room"),
    path("create-room/", views.create_room, name="create-room"),
    path("edit-room/<str:pk>", views.update_room, name="edit-room"),
    path("delete-room/<str:pk>", views.delete_room, name="delete-room"),
    path("delete-message/<str:pk>", views.delete_message, name="delete-message"),
    path("update-user/", views.update_user, name="update-user"),
    path("topics/", views.topics_page, name="topics"),
    path("activity/", views.activity_page, name="activity"),
]
