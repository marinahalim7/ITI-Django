from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect


def display_landing_page(req):
    context={}
    context['name']=req.session['username']
    return render(req, 'landingpage/index.html',context)



