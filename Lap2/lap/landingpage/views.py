from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect


def display_landing_page(req):
    return render(req, 'landingpage/index.html')



