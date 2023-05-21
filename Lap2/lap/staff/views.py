from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import *
def listStaff(req):
    staff = Staff.objects.all()
    return render(req, 'staff/list.html', {'staff': staff})

def insertStaff(req):
    if (req.method == 'GET'):
        return render(req, 'staff/insert.html')
    else:
        Staff.objects.create(name=req.POST['name'])
        return redirect('/staff/list')


def updateStaff(req, id):
    if (req.method == 'GET'):
        return render(req, 'staff/insert.html')
    else:
        Staff.objects.filter(id=id).update(name=req.POST['name'])
        staff = Staff.objects.all()
        return render(req, 'staff/list.html',  {'staff': staff})


def deleteStaff(req, id):
    Staff.objects.get(id=id).delete()
    staff = Staff.objects.all()
    return render(req, 'staff/list.html', {'staff': staff})




