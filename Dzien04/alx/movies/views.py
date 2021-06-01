from django.shortcuts import render
from django.http.response import HttpResponse, Http404
from .models import *
from .forms import *
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings

from django.contrib.auth.decorators import login_required

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
    movie_obj = get_object_or_404(Movie, pk=id)
    comments = Comment.objects.filter(movie=movie_obj)
    return render(request, "movie-details.html",
                  context={"movie": movie_obj,
                           "comments": comments})

@login_required()
def movieadd_response(request):
    #if not request.user.is_authenticated:
    #    return redirect(settings.LOGIN_URL)

    form = MovieForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        movie = form.save(commit=False)
        movie.created_by = request.user
        movie.save()
        return redirect(movielist_response)
    return render(request, "movie-add-2.html",
                  context={
                      "form" : form
                  })

def logout_done(request):
    return render(request, "logout-done.html")
