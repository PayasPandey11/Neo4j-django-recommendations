from django.db import models
from py2neo import authenticate, Graph, Node, Relationship
from screcommend.settings import graph


def suggest_movies(login):
    movies_suggested = graph.data("match (u:User) where u.email contains '%s' match (u)-[:FRIEND]->(ot)-[:RATED]-(rec) where not exists ((u)-[:RATED]->(rec)) return collect(rec.title) as rec,ot.login as name" % (login))
    return movies_suggested
