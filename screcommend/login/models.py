from django.db import models
from py2neo import Node, Relationship
from py2neo import authenticate, Graph
from py2neo.database import Transaction
# set up authentication parameters
authenticate("localhost:7474", "neo4j", "flip6969")
graph = Graph()

user =  graph.find_one("User","name","Payas")
