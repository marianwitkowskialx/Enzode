
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("", startpage_response),
    path("list", movielist_response, name="movie_list"),
    path("movieadd", movieadd_response, name="movie_add"),
    path("list/<int:id>", moviedetails_response, name="movie_details"),
]
