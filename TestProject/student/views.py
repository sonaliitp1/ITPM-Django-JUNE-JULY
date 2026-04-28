from django.shortcuts import render
from .models import Student

# Create your views here.
def show(request):
    obj = Student.objects.all()
    return render(request,'show.html',{'obj':obj})