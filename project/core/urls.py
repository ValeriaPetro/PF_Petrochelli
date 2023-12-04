from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path('', views.home, name="index"),
    path('about/',views.about, name="about"),
    path('contact/',views.about, name="contact"),
    path('faqs/',views.about, name="faqs"),
    path('get_started/',views.about, name="get_started"),
    ]
