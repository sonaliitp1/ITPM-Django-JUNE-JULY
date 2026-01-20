from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from .models import Employee
# Create your views here.
class HomeView(View):
    def get(self,request):
        return render(request,'employee/show.html')

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

class EmpListView(ListView):
    model = Employee
    # context_object_name = 'obj'
    # template_name='emplist.html'


class EmpDetailView(DetailView):
    model = Employee
   
class EmpUpdateView(UpdateView):
    model =Employee

class EmpDeleteView(DeleteView):
    model =Employee

