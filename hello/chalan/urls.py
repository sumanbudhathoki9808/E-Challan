from django.urls import path
from django.contrib.auth import views

from . import views

urlpatterns = [
    path('login/', views.loginPage, name = 'loginPage'),
    # path('register/', views.register, name = 'register'),
    path('', views.home, name = 'home'),
    path('create/', views.create, name = 'create'),
    path('about/', views.about, name = 'about'),
    path('contact/', views.contact, name = 'contact'),
    path('viewchallan/', views.viewchallan, name = 'viewchallan'),
    path('logout/', views.logouts, name = 'logout'),
]