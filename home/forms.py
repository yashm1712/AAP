from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', ]

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class EditProfileForm(ModelForm):
    class Meta:
        model = Member
        fields = ['Graduation_Starting_Year', 'Graduation_Ending_Year', 'Branch', 'PRN_No', 'Final_CGPA',
                  'Mobile_No', 'Profile_Photo', 'Bio', 'Job', 'Project', 'Technical_Skills', 'Hobbies']

        widgets = {
            'Graduation_Starting_Year': forms.Select(attrs={'class': 'form-control'}),
            'Graduation_Ending_Year': forms.Select(attrs={'class': 'form-control'}),
            'Branch': forms.Select(attrs={'class': 'form-control'}),
            'PRN_No': forms.TextInput(attrs={'class': 'form-control'}),
            'Final_CGPA': forms.TextInput(attrs={'class': 'form-control'}),
            'Mobile_No': forms.TextInput(attrs={'class': 'form-control'}),
            'Bio': forms.TextInput(attrs={'class': 'form-control'}),
            'Job': forms.TextInput(attrs={'class': 'form-control'}),
            'Project': forms.TextInput(attrs={'class': 'form-control'}),
            'Technical_Skills': forms.TextInput(attrs={'class': 'form-control'}),
            'Hobbies': forms.TextInput(attrs={'class': 'form-control'}),
        }


class RoleAddFrom(ModelForm):
    class Meta:
        model = Member
        fields = ['Graduation_Starting_Year', 'Graduation_Ending_Year', 'Role']

    widgets = {

        'Role': forms.Select(attrs={'class': 'form-control'}),
        'Graduation_Starting_Year': forms.Select(attrs={'class': 'form-control'}),
        'Graduation_Ending_Year': forms.Select(attrs={'class': 'form-control'}),
    }
