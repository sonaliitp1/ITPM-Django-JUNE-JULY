
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.welcome,name="welcome"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact")
    # add help page

]

'''
App Creation --


1. database connection with help of models 

2. Models create 

3. Admin panel configuration

4. ORM Commnads


create new project --- AppTemplate

App create command -- python manage.py startapp app1
                      django-admin startapp app1 
'''











