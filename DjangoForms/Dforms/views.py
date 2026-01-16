from django.shortcuts import render

from Dforms.forms import registerform

# Create your views here.
def home(request):
    return render(request,'home.html')


def registeru(request):
    uform = registerform()
    return render(request,'register.html',{'f':uform})