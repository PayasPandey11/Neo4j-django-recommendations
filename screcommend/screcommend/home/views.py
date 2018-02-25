from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from py2neo import authenticate, Graph, Node, Relationship
from screcommend.settings import graph
from .models import suggest_friends, rated_movies
# Create your views here.
def index(request):
    login = request.session.get("email")
    movies_rated = rated_movies(login)
    if movies_rated[0]['count(m)'] > 4:
        suggested_friends_names = list()
        fof_names = list()
        sim_movies = list()
        suggested_friends = suggest_friends(login, type="interest")
        fof = suggest_friends(login, type="fof")
        for i in suggested_friends:
            name = i["p2.login"]
            num_movies = i["numbermovies"]
            suggested_friends_names.append(name)
            sim_movies.append(num_movies)
        for i in fof:
            name = i["fof.login"]
            fof_names.append(name)

        context = {
            "suggested_friends": suggested_friends_names,
            "fof": fof_names
        }
        return render(request, 'home/home_index.html', context)
    else:
        movies = rated_movies(None)
        context = {'movies': movies}
        return render(request, 'home/choice.html', context)


@csrf_exempt
def ratings(request):
    if request.method == "POST":
        movie = request.POST.get("movie")
        ratings = request.POST.get("rating")
        login = request.session.get("email")
        User = graph.find_one("User", "email", login)
        movie = graph.find_one("Movie", "title", movie)
        rate = Relationship(User, "RATED", movie, stars=int(ratings))
        graph.merge(rate)

        movies_rated = rated_movies(login)
        if movies_rated[0]['count(m)'] > 4:
            return HttpResponse("5")
        else:
            return HttpResponse(movies_rated[0]['count(m)'])


@csrf_exempt
def follow(request):
        if request.method == "POST":
            username = request.POST.get("username")
            login = request.session.get("email")
            follow_status = request.POST.get("follow_status")
            User = graph.find_one("User", "email", login)

            friend = graph.find_one("User", "login", username)
            if follow_status == "Follow":

                follow = Relationship(User, "FRIEND", friend)
                graph.merge(follow)

            if follow_status == "Unfollow":
                graph.run("Match (u:User) where u.email contains '%s' match (u)-[f:FRIEND]->(otherPerson) where otherPerson.login contains '%s' Delete f" % (login, username))

            return HttpResponse(follow_status)
