from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_users, name="login_users"),
]