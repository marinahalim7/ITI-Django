from django.urls import path
from .views import *
urlpatterns = [
   path('login/', display_login_page, name='loginPagePath'),
   path('register/', display_register_page, name='registerPagePath'),
   path('home/', display_home_page, name='homePagePath'),
   path('logout/', LogOut, name='logoutPath'),
]
