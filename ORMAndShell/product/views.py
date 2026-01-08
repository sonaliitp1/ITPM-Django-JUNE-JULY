from django.shortcuts import render,redirect
from .models import ProductInfo

# Create your views here.

def home(request):
    return render(request,'home.html')

def showproduct(request):
    data = ProductInfo.objects.all()

    context ={'d':data}

    return render(request,'showproducts.html',context)

def addproduct(request):
    if request.method=="POST":
        pid = request.POST.get("pid")
        pname = request.POST.get("pname")
        category = request.POST.get("category")
        stock = request.POST.get("stock")
        obj = ProductInfo(pid,pname,category,stock)
        obj.save()
        return redirect("show")
    else:          
        return render(request,"addproduct.html")