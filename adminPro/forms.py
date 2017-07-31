from django.contrib.auth.models import User
from django import forms



class UserForm(forms.ModelForm):
    GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),

    )
    password = forms.CharField(widget = forms.PasswordInput())
    firstname =  forms.CharField(max_length=250)
    lastname =  forms.CharField(max_length=250)
    phone = forms.CharField(max_length=256)
    gender = forms.ChoiceField( choices =GENDER, required = True)

    class Meta():
        model = User
        fields = ("username","email","password")
