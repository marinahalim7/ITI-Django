from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.


def index(req):
    if (req.method == 'GET'):
        return HttpResponse("List Students")
    else:
        return HttpResponse("Acsses denied")


def insert(req):
    if (req.method == 'GET'):
        return render(req, 'student/insert.html')
    else:
        return HttpResponseRedirect('/students')


def update(req,id):
    if (req.method == 'GET'):
        return render(req, 'student/update.html')
    else:
        return HttpResponseRedirect('/students')


def delete(req,id):
    if (req.method == 'GET'):
        return HttpResponseRedirect('/students')
