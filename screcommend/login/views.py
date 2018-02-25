from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.core import management
import datetime
from py2neo import authenticate, Graph, Node, Relationship
from py2neo.database import Transaction
import crypt
from screcommend.settings import graph


def index(request):
    if request.session.get("email"):
        return redirect('/home')
    else:
        return render(request, 'login/index.html')


@csrf_exempt
def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email").lower()
        password = request.POST.get("password")
        password = crypt.crypt(password)
        User = graph.data("MATCH (n:User) WHERE n.login = '%s' OR n.email ='%s' RETURN count(n) , n" % (username, email))

        if User:
            if User[0]["n"]["email"] == email:
                return HttpResponse("Email exists")
            else:
                return HttpResponse("Username exists")
        else:
            tx = graph.begin()
            a = Node("User", name=username, login=username, email=email, password=password)
            tx.create(a)
            tx.commit()
            request.session['email'] = email
            return HttpResponse("Success")


@csrf_exempt
def signin(request):
    if request.method == "POST":
        email = request.POST.get("email").lower()
        password = request.POST.get("password")
        User = graph.data("MATCH (n:User) WHERE n.email ='%s' RETURN  n" % (email))
        if User:
            valid_password = crypt.crypt(password, User[0]["n"]["password"]) == User[0]["n"]["password"]
            if valid_password:
                print("user in")
                request.session['email'] = email
                return HttpResponse("Success")
            else:
                return HttpResponse("Wrong Password")
        else:
            return HttpResponse("User does not exists")


def logout(request):
    try:
        del request.session['email']
    except KeyError:
        pass
    return redirect('/')
