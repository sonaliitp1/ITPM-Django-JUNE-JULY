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
    
def edit(request,id):
    obj =  ProductInfo.objects.get(pid=id)
    context={'obj':obj}
    if request.method == "POST":
        pid = request.POST.get("pid")
        pname = request.POST.get("pname")
        category = request.POST.get("category")
        stock = request.POST.get("stock")
        obj.pid = pid
        obj.pname = pname 
        obj.category =category
        obj.stock = stock
        obj.save()
        return redirect("show")
    else:
        return render(request,'edit.html',context)
    
def delete(request,id):
    obj = ProductInfo.objects.get(pid=id)
    obj.delete()
    return redirect("show")