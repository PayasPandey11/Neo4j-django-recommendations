from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/',views.signup,name="signup"),
    path('signin/',views.signin,name="signin"),
    path('logout/',views.logout,name="logout")
    ]
