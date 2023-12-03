from django.urls import path
from . import views

app_name = "get_started"

urlpatterns = [
    path('', views.home, name="index"),
]
