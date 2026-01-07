from django.shortcuts import render
from .models import ProductInfo

# Create your views here.

def home(request):
    return render(request,'home.html')

def showproduct(request):
    data = ProductInfo.objects.all()

    context ={'d':data}

    return render(request,'showproducts.html',context) 