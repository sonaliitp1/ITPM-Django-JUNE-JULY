from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from .models import Employee


# Create your views here.

class HomeView(View):
    def get(self,request):
        return HttpResponse("Hello Students")

    def post(self,request):
        name = request.POST.get("name")
        age = request.POST.get("age")
        context ={"name":"ABC","age":20}
        return render(request,'home.html',context)
       
class ShowView(TemplateView):
    template_name ='show.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employees'] = Employee.objects.all()
        context["name"] ="ABC"
        context["age"] = 20
        return context
        
# def home(request):
#      return HttpResponse("Hello Students")

