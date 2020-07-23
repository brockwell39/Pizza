from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password']
        help_texts = {
            'username': None,
            'email': None,
        }
        widgets = {
            'username': forms.TextInput(attrs={
            'class': 'form-control',}),
            'email': forms.EmailInput(attrs={
            'class': 'form-control',
            'id':'special'}),
            'first_name': forms.TextInput(attrs={
            'class': 'form-control',}),
            'last_name': forms.TextInput(attrs={
            'class': 'form-control',}),
            'password': forms.PasswordInput(attrs={
            'class': 'form-control',}),
        }
