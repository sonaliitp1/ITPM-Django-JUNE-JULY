
from django.urls import path
from .import views
from .views import HomeView
from .views import ShowView

urlpatterns = [
    
    # path('',views.home,name='home')
    path('',HomeView.as_view(),name='Home'),
    path('show/',ShowView.as_view(),name='show')
]
