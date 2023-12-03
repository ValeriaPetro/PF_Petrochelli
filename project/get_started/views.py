from django.shortcuts import render

def home(request):
    return render(request, "get_started/index.html")
