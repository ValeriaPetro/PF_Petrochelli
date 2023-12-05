from django.urls import path
from . import views

app_name = "get_started"

urlpatterns = [
    path('', views.home, name="index"),
    path('create_users_manually/', views.create_users_manually),
    path('create_users/', views.create_users),
    path('search/', views.search),
]
