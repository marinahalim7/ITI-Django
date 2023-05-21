from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.


def list_students(req):
    if (req.method == 'GET'):
        return HttpResponse("List Students")


def list_staff(req):
    if (req.method == 'GET'):
        return HttpResponse("List Staff")
