
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse


# Create your views here.


def index(req):
    if (req.method == 'GET'):
        return HttpResponse("List Staff")
    else:
        return HttpResponse("Acsses denied")


def insert(req):
    if (req.method == 'GET'):
        return JsonResponse({'name': 'Marina'})


def update(req,id):
    if (req.method == 'GET'):
        return JsonResponse({'name': 'Marina'})

def delete(req,id):
    if (req.method == 'GET'):
        return HttpResponseRedirect('/staff')
