from django.shortcuts import render
from django.http.response import HttpResponse, Http404
from .models import *
from .forms import *
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings

# Create your views here.

def startpage_response(request):
    return HttpResponse("<br/>".join( dir(request) ) )

def movielist_response(request):
    all_movies = Movie.objects.all().order_by("title")
    return render(request, "movie-list.html",
                  context={"movies":all_movies,
                           "media_url": settings.MEDIA_URL } )

def moviedetails_response(request, id):
    # try:
    #     movie = Movie.objects.get(pk=id)
    #     print(movie)
    #     return HttpResponse(str(movie))
    # except:
    #     raise Http404("nie ma takiego filmu")
    movie = get_object_or_404(Movie, pk=id)
    return render(request, "movie-details.html",
                  context={"movie": movie})

def movieadd_response(request):
    form = MovieForm()
    return render(request, "movie-add-1.html",
                  context={
                      "form" : form
                  })