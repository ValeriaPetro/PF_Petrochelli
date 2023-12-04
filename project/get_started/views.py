from django.shortcuts import render, redirect

from . import models
from datetime import date

def home(request):
    User = models.User.objects.all()
    context = {"Users": User}
    return render(request, "get_started/index.html", context)

def create_users_misc(request):
    p1 = models.Country(name="United States")
    p2 = models.Country(name="United Kingdom")
    p3 = models.Country(name="Poland")
    p1.save()
    p2.save()
    p3.save()
    
    u1 = models.User(name="Robert", last_name="Pattinson", email_address="none", company = "Batman&Co.", country_of_benchmark = 1, region_of_benchmark = 1)
    u2 = models.User(name="Robert", last_name="Junior", email_address="none", company = "IronMan.", country_of_benchmark = 2, region_of_benchmark = 2)
    u3 = models.User(name="Robin", last_name="Rago", email_address="none", company = "Batman&Co.", country_of_benchmark = 3, region_of_benchmark = 3)
    u1.save()
    u2.save()
    u3.save()
    return redirect("get_started:index")


from . import forms

def create_users(request):
    if request.method == "POST":
        form = forms.UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("get_started:index")
        
    else: 
        form = forms.UserForm
    return render(request, "get_started/create_users.html", {"form": form})
