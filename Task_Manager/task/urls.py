from django.contrib import admin
from django.urls import path
from .views import All_Task

urlpatterns = [
    path('all_task',All_Task.as_view()),
]

# https://identity.getpostman.com/client-auth/confirm?auth_challenge=0141232f3f2bd77158f7215babb9eb998aaaa6fdb5bcde67dc6d60fde296bef1&auth_device=app_native&auth_device_version=11.39.2