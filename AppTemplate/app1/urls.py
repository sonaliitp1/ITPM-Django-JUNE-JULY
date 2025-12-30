
from django.urls import path
from .import views

urlpatterns = [

    path('profile/',views.profile,name="profile"),
    path('services/',views.services,name="services")
    
]