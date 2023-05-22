from django import forms


class RegisterForm(forms.Form):
    name = forms.CharField(required=True, min_length=2)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)


class LoginForm(forms.Form):
        email = forms.EmailField(required=True)
        password = forms.CharField(required=True, min_length=5)