from django.urls import path
from .import views

urlpatterns = [
   
   
   path('loginuser/',views.loginu,name='loginu'),
   path('registeruser/',views.registeru,name='registeru'),
   path('logoutuser/',views.logoutu,name='logoutu')
]
