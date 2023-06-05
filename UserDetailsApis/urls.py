from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^signup$', views.signup, name="signup"),
    re_path(r'^addUserDetails$', views.addUser, name="addUser"),
    re_path(r'^updateUserDetails$', views.updateUser, name="updateUser"),
    re_path(r'^deleteUsers$', views.deleteUser, name="deleteUser"),
]