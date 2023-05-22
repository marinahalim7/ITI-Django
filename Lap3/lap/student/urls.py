from django.urls import path
from .views import *
urlpatterns = [
   path('list/', list_students, name='listStudentPath'),
   path('insert/', insert_student, name='insertStudentPath'),
   path('update/<int:id>/', update_student, name='updateStudentPath'),
   path('delete/<int:id>/', delete_student, name='deleteStudentPath'),

]