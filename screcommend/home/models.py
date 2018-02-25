from django.db import models
from py2neo import authenticate, Graph, Node, Relationship
from screcommend.settings import graph
# Create your models here.


def suggest_friends(login,type="interest"):
    if type == "interest":
        suggested_friends = graph.data("MATCH (p1:User {email: '%s'})-[x:RATED]->(m:Movie)<-[y:RATED]-(p2:User) WHERE NOT EXISTS( (p1)-[:FRIEND]->(p2)) WITH COUNT(m) AS numbermovies, SUM(x.stars * y.stars) AS xyDotProduct, SQRT(REDUCE(xDot=0.0, a IN COLLECT(x.stars) | xDot + a ^ 2)) AS xLength, SQRT(REDUCE(yDot = 0.0, b IN COLLECT(y.stars) | yDot + b^2)) AS yLength, p1, p2 RETURN p2.login,numbermovies ORDER BY xyDotProduct / (xLength * yLength) DESC LIMIT 100;" % (login))
        return (suggested_friends)
    elif type == "fof":
        fof = graph.data("Match (u:User) where u.email contains '%s' Match(u)-[: FRIEND] -> (otherperson) - [: FRIEND]->(fof) WHERE NOT EXISTS( (u)-[:FRIEND]->(fof) ) return fof.login,fof.name"%(login))
        return (fof)


def rated_movies(login):
    if login:
        movies_rated = graph.data("Match (u:User)-[:RATED]->(m:Movie) Where u.email contains '%s' return count(m)" % (login))
        return movies_rated
    else:
        movies = graph.data("Match (m:Movie)<-[r:RATED]-() return m,Count(*) AS num ORDER BY num desc Limit 25")
        return movies
