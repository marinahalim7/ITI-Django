from django import forms

class AddStaffForm(forms.Form):
    name=forms.CharField(required=True,min_length=2,max_length=10)
