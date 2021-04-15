from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, "login.html")

def home(request):
    return render(request, "home.html")

def create(request):
    return render(request, "create.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")
