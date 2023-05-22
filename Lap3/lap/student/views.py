from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views import View
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required


@login_required()
def list_students(req):
    students = Student.objects.all()
    context = {}
    context['students'] = students
    context['name'] = req.session['username']
    return render(req, 'student/list.html', context)


def insert_student(req):
    if (req.method == 'GET'):
        context = {}
        context['form'] = AddStudentForm()
        context['name'] = req.session['username']
        return render(req, 'student/insert.html', context)
    else:
        form = AddStudentForm(req.POST)
        if (form.is_valid()):
            Student.objects.create(first_name=req.POST['first_name'],
                                   last_name=req.POST['last_name'],
                                   email=req.POST['email'],
                                   staffRef=Staff.objects.get(id=req.POST['staffRef']))
            students = Student.objects.all()
            context = {}
            context['students'] = students
            context['name'] = req.session['username']
            return render(req, 'student/list.html', context)


def update_student(req, id):
    context = {}
    context['form'] = AddStudentForm()
    context['name'] = req.session['username']
    if (req.method == 'GET'):
        return render(req, 'student/insert.html', context)
    else:
        form = AddStudentForm(req.POST)
        if (form.is_valid()):
            Student.objects.filter(id=id).update(first_name=req.POST['first_name'],
                                                 last_name=req.POST['last_name'],
                                                 email=req.POST['email'],
                                                 staffRef=Staff.objects.get(id=req.POST['staffRef']))
            students = Student.objects.all()
            return render(req, 'student/list.html', {'students': students})


def delete_student(req, id):
    Student.objects.get(id=id).delete()
    students = Student.objects.all()
    return render(req, 'student/list.html', {'students': students})
