from django.shortcuts import render
from django.http.response import HttpResponse, Http404
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.

def startpage_response(request):
    return HttpResponse("<br/>".join( dir(request) ) )

def movielist_response(request):
    all_movies = Movie.objects.all().order_by("title")
    return render(request, "movie-list.html",
                  context={"movies":all_movies} )