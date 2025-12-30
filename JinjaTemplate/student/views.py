from django.shortcuts import render

# Create your views here.
def data(request):
    name ="Raj"
    age = 22
    city ="Pune"
    course="Python"
    context ={"stuname":name,"age":age,"city":city,"course":course}
    return render(request,'data.html',context)

def skills(request):
    courses = ["C","C++","Java","Python","Android"]
    context ={"c":courses}
    return render(request,"skills.html",context)