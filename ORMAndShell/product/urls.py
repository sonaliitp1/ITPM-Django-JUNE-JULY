
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('s/',views.showproduct,name='show'),
    path('a/',views.addproduct,name='add'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('delete/<int:id>',views.delete,name='delete')
]
