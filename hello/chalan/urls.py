from django.urls import path
from django.contrib.auth import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    
    # path('register/', views.register, name = 'register'),
    path('', views.home, name = 'home'),
    path('logins/', views.loginPage, name = 'loginPage'),
    path('create/', views.create, name = 'create'),
    path('about/', views.about, name = 'about'),
    path('contact/', views.contact, name = 'contact'),
    path('viewchallan/', views.viewchallan, name = 'viewchallan'),
    path('logout/', views.logouts, name = 'logout'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()