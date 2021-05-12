from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('\create', views.create, name = 'create'),
    path('\about', views.about, name = 'about'),
    path('\contact', views.contact, name = 'contact'),
    
]
