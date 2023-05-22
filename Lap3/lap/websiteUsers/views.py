from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate
from .models import *
from .forms import *
def display_login_page(req):
    context = {}
    context['form'] = LoginForm()

    if (req.method == 'GET'):
        return render(req, 'websiteUsers/login.html',context)
    else:
        form=LoginForm(req.POST)
        if(form.is_valid()):
            user = websiteUsers.objects.filter(email=req.POST['email'], password=req.POST['password'])
            if user.exists():
                req.session['username']=user[0].name
                return redirect('/users/home')
            else:
                context['invalid'] = "Invalid email or password!"
                return render(req, 'websiteUsers/login.html', context)


def display_register_page(req):
    context = {}
    context['form'] = RegisterForm()
    if (req.method == 'GET'):
        return render(req, 'websiteUsers/register.html',context)
    else:
        form = RegisterForm(req.POST)
        if (form.is_valid()):
            user = websiteUsers.objects.filter(email=req.POST['email'])
            if (len(user)!=0):
                context['emailerror']="This email is already token!"
                return render(req, 'websiteUsers/register.html', context)
            else:
                websiteUsers.objects.create(name=req.POST['name'],
                                            email=req.POST['email'],
                                            password=req.POST['password'])
                return redirect('/users/login')

        else:
            context['invalid']
            return render(req, 'websiteUsers/register.html', context)


def display_home_page(req):
    if (req.method == 'GET'):
        context={}
        context['name']=req.session['username']
        return render(req, 'websiteUsers/home.html',context)

def LogOut(req):
    req.session.clear()
    context = {}
    context['form'] = LoginForm()
    return render(req, 'websiteUsers/login.html', context)
