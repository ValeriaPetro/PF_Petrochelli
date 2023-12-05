from django.shortcuts import render

def home(request):
    return render(request, "core/index.html")

def about(request):
    return render(request, "core/about.html")

def get_started(request):
    return render(request, "get_started/index.html")

def contact(request):
    return render(request, "contact/index.html")

def faqs(request):
    return render(request, "faqs/index.html")


def users(request):
    all_users = []
    for user in User.objects.all():
        all_users.append(user)
        
    context = {"users": all_users}
    
    return render(request, "users/index.html", context)