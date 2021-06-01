
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("", startpage_response),
    path("list", movielist_response, name="movie_list")
]
