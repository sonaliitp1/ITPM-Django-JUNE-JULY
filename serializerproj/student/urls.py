
from django.urls import path,include
from .views import get_students

urlpatterns = [
      
    path('students/get/', get_students),
]
