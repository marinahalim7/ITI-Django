from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect


def list_students(req):
    return HttpResponse("List of Students")


def list_staff(req):
    return HttpResponse("List of Staff")