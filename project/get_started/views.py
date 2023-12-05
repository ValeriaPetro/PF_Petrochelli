from django.shortcuts import render, redirect

from . import models
from datetime import date

# funcion anterior - lo "nuevo" es para crear usuarios desde la aplicacion get_started
# def home(request):
#     return render(request, "get_started/index.html")

def home(request):
    users = models.User.objects.all()
    context = {"users": users}
    return render(request, "get_started/index.html", context)

def create_users_manually(request):
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
    return redirect("core/index.html")

def search(request):
    # búsqueda por empresa que contenga "Batman"
    company = models.User.objects.filter(company="Batman")

    # búsqueda por pais de benchmark que sea igual a "China"
    country_of_benchmark = models.User.objects.filter(country_of_benchmark=1)

    context = {
        "company": company,
        "country_of_benchmarl": country_of_benchmark,
    }
    return render(request, "get_started/search.html", context)

from . import forms

# def home(request):
#     users = models.User
#     return render(request, "get_started/index.html")

def create_users(request):
    if request.method == "POST":
        form = forms.UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("get_started:index.html")
        
    else: 
        form = forms.UserForm()
    return render(request, "get_started/create_users.html", {"form": form})
