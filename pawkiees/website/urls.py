from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('sitters/', views.sitters, name='sitters'),
    path('booking/', views.booking, name='booking'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]