
from django.urls import path
from .import views
urlpatterns = [
   
   path('',views.home,name='home'),
   path('loginu/',views.loginu,name='loginu'),
   path('dashboard/',views.dashboard,name='dash'),
   path('services/',views.services,name='services'),
   path('logoutu/',views.logoutu,name='logout')

]
