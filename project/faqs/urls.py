from django.urls import path
from . import views

app_name = "faqs"

urlpatterns = [
    path('', views.home, name="index"),
]
