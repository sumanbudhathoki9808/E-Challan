# from django.shortcuts import render, redirect
# # from .model import *
from django.views.decorators.csrf import csrf_exempt
# from django.contrib.auth.forms import UserCreationForm

# Create your views here.

from .form import CreateUserForm



from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import challan
from . import models

# Create your views here.
# from .models import *
# from .forms import CreateUserForm


def register(request):
    # forms = CreateUserForm()

    # if request.method == 'POST':
    #     forms = CreateUserForm(request.POST)
    #     if forms.is_valid():
    #         forms.save()

    # context = {'form': forms}

    forms = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account created sucessfully for '+ user)
        return redirect('/')

    # return render(request,'signin.html',{"form":form})
    # context = {'form': forms}

    return render(request, "register.html", {'form': forms})

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)
       
        if user is not None:
            login(request,user)
            return redirect('/create')
        else:
            messages.info(request, 'Username or password is incorrect')

    context = {}
    return render(request,'login.html',context)

def home(request):
    return render(request, "home.html")

def create(request):
    if request.method == "POST":
        # challans = challan()
        names = request.POST.get('names')
        phonenumber = request.POST.get('phonenumber')
        place = request.POST.get('place')
        licensenumber = request.POST.get('licensenumber')
        vehiclenumber = request.POST.get('vehiclenumber')
        vehicletype = request.POST.get('vehicletype')
        creator = request.POST.get('creator')

        ins = models.challan(names = names, phonenumber = phonenumber,  place=place, licensenumber = licensenumber, vehiclenumber=vehiclenumber, vehicletype=vehicletype, creator=creator)
        ins.save()

    return render(request, "create.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")


def viewchallan(request):

    rec = challan.objects.filter(creator = request.user)

    return render(request, "viewchallan.html", {"record" : rec })
