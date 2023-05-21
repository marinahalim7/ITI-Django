from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import *
from staff.models import *


def list_students(req):
    students = Student.objects.all()
    return render(req, 'student/list.html', {'students': students})


def insert_student(req):
    if (req.method == 'GET'):
        staffCollection = Staff.objects.all()
        return render(req, 'student/insert.html', {'staffCollection': staffCollection})
    else:
        Student.objects.create(first_name=req.POST['first_name'],
                               last_name=req.POST['last_name'],
                               email=req.POST['email'],
                               staffRef=Staff.objects.get(id=req.POST['staffid']))

        return redirect('/students/list')


def update_student(req, id):
    if (req.method == 'GET'):
        staffCollection = Staff.objects.all()
        return render(req, 'student/insert.html', {'staffCollection': staffCollection})
    else:
        Student.objects.filter(id=id).update(first_name=req.POST['first_name'],
                                             last_name=req.POST['last_name'],
                                             email=req.POST['email'],
                                             staffRef=Staff.objects.get(id=req.POST['staffid']))
        students = Student.objects.all()
        return render(req, 'student/list.html', {'students': students})


def delete_student(req, id):
    Student.objects.get(id=id).delete()
    students = Student.objects.all()
    return render(req, 'student/list.html', {'students': students})
