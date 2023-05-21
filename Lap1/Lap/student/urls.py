from django.urls import path
from .views import *
urlpatterns = [
    path('', index),
    path('create', insert),
    path('del/<int:id>', delete),
    path('upd/<int:id>', update),

]
