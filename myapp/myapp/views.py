from django.http import HttpResponse
from django.shortcuts import render

def welcome(request):
    return render(request,'welcome.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
 

