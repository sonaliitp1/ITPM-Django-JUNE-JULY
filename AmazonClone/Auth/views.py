from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')


def loginu(request):
    return render(request,'loginu.html')

def registeru(request):
    pass 

def logoutu(request):
    pass
