from django.urls import path
from . import models

urlpatterns = [
    path("", views.post_list, name="post_list"),
]
