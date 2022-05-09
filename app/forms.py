from django import forms
from django.forms import ModelForm
from .models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['Name', 'Email', 'Phone', 'City']

        # widgets = {
        #     'Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Saisir votre nom ici'}),
        #     'Email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Saisir votre adresse-email ici'}),
        #     'Phone': forms.IntegerField(attrs={'placeholder': 'votre numero'}),
        #     'City': forms.TextInput(attrs={'placeholder': 'la ville'}),
        # }