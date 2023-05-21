from django.urls import path
from .views import *
urlpatterns = [
   path('', display_landing_page, name='landingPagePath'),


]