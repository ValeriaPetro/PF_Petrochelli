from django.urls import path
from . import views

app_name = "get_started"

urlpatterns = [
    path('', views.home, name="index"),
    path('create_users_misc/', views.create_users, name="create_users_misc"),
    path('create_users/', views.create_users),
]
