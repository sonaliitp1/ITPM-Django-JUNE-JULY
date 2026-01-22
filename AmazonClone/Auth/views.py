from django.shortcuts import render,redirect
from django.contrib.auth.models import User

# Create your views her
def home(request):
    return render(request,'home.html')


def loginu(request):
    return render(request,'loginu.html')

def registeru(request):
    if request.method =="POST":
        un = request.POST.get("username")
        em = request.POST.get("email")
        password = request.POST.get("password")
        cpassword = request.POST.get("cpassword")
        obj = User.objects.filter(username=un).exists()
        if obj:
            return render(request,'registeru.html',{'error':"User Is Already Exists....Please try again"})
        elif password!=cpassword:
             return render(request,'registeru.html',{'error':"Password and ConfirmPassword do not match"})
        else:
            obj = User(username=un,email=em,password=password)
            obj.save()
            return redirect("loginu")
    else:
        return render(request,'registeru.html')

def logoutu(request):
    pass
