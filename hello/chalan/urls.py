from django.urls import path
from django.contrib.auth import views

from django.contrib.auth import views as auth_views
from users import views as user_views

from . import views

urlpatterns = [
    path('', views.loginPage, name = 'loginPage'),
    path('register/', views.register, name = 'register'),
    path('home/', views.home, name = 'home'),
    path('create/', views.create, name = 'create'),
    path('about/', views.about, name = 'about'),
    path('contact/', views.contact, name = 'contact'),

    path('profile/', views.contact, name = 'profile'),

    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name = 'logout'),


]