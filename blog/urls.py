from django.contrib import admin
from django.urls import path
from blog.views import TestView

urlpatterns = [
    path("", TestView.as_view()),
]
