from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


from .models import *
from .forms import *
@login_required
def listStaff(req):
    context = {}
    context['name'] = req.session['username']
    context['staff'] =Staff.objects.all()
    return render(req, 'staff/list.html', context)

def insertStaff(req):
    context={}
    context['name'] = req.session['username']


    if (req.method == 'GET'):
        context['form'] = AddStaffForm()
        return render(req, 'staff/insert.html',context)
    else:
        form=AddStaffForm(req.POST)
        if(form.is_valid()):
             Staff.objects.create(name=req.POST['name'])
             return render(req, 'staff/list.html', context)




def updateStaff(req, id):
    context = {}
    context['name'] = req.session['username']

    if (req.method == 'GET'):
        context['form'] = AddStaffForm()
        return render(req, 'staff/insert.html',context)
    else:
        form = AddStaffForm(req.POST)
        if (form.is_valid()):
            Staff.objects.filter(id=id).update(name=req.POST['name'])
            staff = Staff.objects.all()
            return render(req, 'staff/list.html', {'staff': staff})


def deleteStaff(req, id):
    Staff.objects.get(id=id).delete()
    staff = Staff.objects.all()
    return render(req, 'staff/list.html', {'staff': staff})




