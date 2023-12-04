from django.shortcuts import render

def home(request):
    return render(request, "core/index.html")

def about(request):
    return render(request, "about/index.html")

def get_started(request):
    return render(request, "get_started/index.html")

def contact(request):
    return render(request, "contact/index.html")

def faqs(request):
    return render(request, "faqs/index.html")