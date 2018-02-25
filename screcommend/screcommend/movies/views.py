from django.shortcuts import render

from .models import suggest_movies
# Create your views here.
def index(request):
    login = request.session.get("email")
    movies_suggested = suggest_movies(login)
    print(movies_suggested)
    context = {"recommedation": movies_suggested}
    #print(context["recommedation"])
    return render(request, 'movies/movies_index.html', context)
