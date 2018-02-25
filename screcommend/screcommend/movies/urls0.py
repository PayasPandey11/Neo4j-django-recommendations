from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ratings/', views.ratings, name='ratings'),
    path('follow/', views.follow, name='follow')
    ]
