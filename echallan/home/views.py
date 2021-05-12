from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from .models import Challan
# Create your views here.


def home(request):
    return render(request,'home.html')

@login_required
def create(request):
    if request.method == "POST":
        challans = Challan()
        names = request.POST.get('names')
        phonenumber = request.POST.get('phonenumber')
        place = request.POST.get('place')
        licensenumber = request.POST.get('licensenumber')
        vehiclenumber = request.POST.get('vehiclenumber')
        vehicletype = request.POST.get('vehicletype')
        creator = request.POST.get('creator')

        challans.names = names
        challans.phonenumber = phonenumber
        challans.place = place
        challans.licensenumber = licensenumber
        challans.vehiclenumber = vehiclenumber
        challans.vehicletype = vehicletype
        challans.creator = creator
        challans.save()

    return render(request, "create.html")

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')


