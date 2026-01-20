
from django.urls import path
from .import views
from .views import HomeView
from .views import ShowView
from .views import EmpListView
from .views import EmpDetailView
urlpatterns = [
    
    # path('',views.home,name='home')
    path('',HomeView.as_view(),name='Home'),
    path('show/',ShowView.as_view(),name='show'),
    path('emplist/',EmpListView.as_view(),name='emplist'),
    path('empdetail/<int:pk>',EmpDetailView.as_view(),name='empdetail')
]
