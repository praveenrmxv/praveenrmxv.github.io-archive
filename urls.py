from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name="contact"),
    path('search/', views.search, name="search"),
    path('signup', views.handleSignUp, name="handleSignUp"),
    path('login', views.handleLogin, name="handleSignUp"),
    path('logout', views.hanldeLogout, name="handleSignUp"),


]
