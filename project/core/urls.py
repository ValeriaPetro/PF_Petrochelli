from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path('', views.home, name="index"),
    path('about/',views.about, name="about"),
    path('get_started/',views.get_started, name="get_started"),
    ]
