from django.shortcuts import render,redirect

from cars.forms import carforms
from .models import cars

# Create your views here.
def home(request):

    obj = cars.objects.all()
    return render(request,'home.html',{'obj':obj})


def register(request):
     form = carforms()
     return render(request ,'register.html',{'form':form})


def add_car(request):
    if request.method == 'POST':
        form = carforms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = carforms()

    return render(request, 'car_form.html', {'form': form})

    
