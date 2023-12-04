from django.shortcuts import render

def home(request):
    return render(request, "core/index.html")

def about(request):
    return render(request, "core/about.html")

def get_started(request):
    return render(request, "get_started/index.html")