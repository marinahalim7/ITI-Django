from django import forms
from staff.models import *
class AddStudentForm(forms.Form):
    first_name=forms.CharField(required=True,min_length=2,max_length=10)
    last_name = forms.CharField(required=True, min_length=2, max_length=10)
    email=forms.EmailField(required=True)
    staffRef=forms.ChoiceField(required=True,label="Staff",choices=[(staff.id,staff.name)for staff in Staff.objects.all()])

