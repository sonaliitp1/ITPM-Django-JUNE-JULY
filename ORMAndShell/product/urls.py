
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('s/',views.showproduct,name='show')
]
