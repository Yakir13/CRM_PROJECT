from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("record_db", views.record_db, name="record_db"),
    path("create_record", views.create_record, name="create_record"),
    path("update_record/<int:pk>", views.update_record, name="update_record"),
    path("record/<int:pk>", views.singel_record, name="record"),
    path("delete_record/<int:pk>", views.delete_record, name="delete_record"),
]
