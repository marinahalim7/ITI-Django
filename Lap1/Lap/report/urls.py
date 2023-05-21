from django.urls import path
from .views import *
urlpatterns = [
    path('students', list_students),
    path('staff', list_staff),


]
