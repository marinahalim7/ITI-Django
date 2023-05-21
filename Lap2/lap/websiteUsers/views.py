from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate
from .models import *
def display_login_page(req):
    if (req.method == 'GET'):
        return render(req, 'websiteUsers/login.html')
    else:
        user = websiteUsers.objects.filter(email=req.POST['email'], password=req.POST['password'])
        if user.exists():
            return redirect('/users/home')
        else:
            return render(req, 'websiteUsers/login.html')


def display_register_page(req):
    if (req.method == 'GET'):
        return render(req, 'websiteUsers/register.html')
    else:
        websiteUsers.objects.create(name=req.POST['name'],
                                   email=req.POST['email'],
                                   password=req.POST['password'])

        return redirect('/users/login')

def display_home_page(req):
    if (req.method == 'GET'):
        return render(req, 'websiteUsers/home.html')


