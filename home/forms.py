from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', ]


class EditProfileForm(ModelForm):
    class Meta:
        model = Member
        fields = ['Graduation_Starting_Year', 'Graduation_Ending_Year', 'Branch', 'PRN_No', 'Final_CGPA',
                  'Mobile_No', 'Profile_Photo', 'Bio', 'Job', 'Project', 'Technical_Skills', 'Hobbies']


class RoleAddFrom(ModelForm):
    class Meta:
        model = Member
        fields = ['Role']
