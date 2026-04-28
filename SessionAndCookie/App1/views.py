from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    return render(request,'home.html')

def loginu(request):
     if request.method=="POST":
          un = request.POST.get("uname")
          ps = request.POST.get("password")
          if un=="john" and ps =="john123":
               request.session['username'] = un
               request.session['is_logged_in'] = True
               return redirect("dash")
                #return render(request,'Dashboard.html')
          
          else:
               return render(request,'login.html',{'error':"Invalid Credentials"})
  
     else:
          return render(request,'login.html')

def dashboard(request):
     if request.session.get('is_logged_in'):
        username = request.session.get('username')
        return render(request, "Dashboard.html", {"username": username})
     else:
        return render(request,"login.html",{"error":"Please Login First..."})

    # return render(request,'Dashboard.html')

def services(request):
     if request.session.get('is_logged_in'):
        username = request.session.get('username')
        return render(request, "services.html", {"username": username})
     else:
        return render(request,"login.html",{"error":"Please Login First..."})

     


def logoutu(request):
     request.session.flush()   # Clears entire session
     return redirect("loginu")


