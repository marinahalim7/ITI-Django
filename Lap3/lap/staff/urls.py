from django.urls import path
from .views import *
urlpatterns = [
   path('list/', listStaff, name='listStaffPath'),
   path('insert/', insertStaff, name='insertStaffPath'),
   path('update/<int:id>/', updateStaff, name='updateStaffPath'),
   path('delete/<int:id>/', deleteStaff, name='deleteStaffPath'),

]