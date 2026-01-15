from django.shortcuts import render
from .models import cars

# Create your views here.
def home(request):

    obj = cars.objects.all()
    return render(request,'home.html',{'obj':obj})