
from django.urls import path
from .import views

urlpatterns = [
   
   path('students/getall',views.get_students),
   path('students/createstudent',views.create_student),
   path('students/deletestudent/<int:id>',views.delete_student),
   path('students/updatestudent/<int:id>',views.update_student),
   path('students/patchstudent/<int:id>',views.patch_student)
]

