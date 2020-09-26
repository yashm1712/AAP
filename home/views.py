from django.contrib import messages
from django.shortcuts import render, redirect
# this is my comment
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime

from .decorators import unauthenticated_user
from .forms import CreateUserForm, EditProfileForm, RoleAddFrom
from .models import *


def home(request):
    return render(request, 'home/home.html')


@unauthenticated_user
def register(request):
    form = CreateUserForm()
    role_form = RoleAddFrom()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        role_form = RoleAddFrom(request.POST)

        if form.is_valid() and role_form.is_valid():
            user = form.save()
            role = role_form.save(commit=False)
            role.user = user
            role.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('/login')

    context = {'form': form, 'role_form': role_form}
    return render(request, 'home/register.html', context)


@unauthenticated_user
def login_validate(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            print('User')
            login(request, user)
            user = User.objects.get(username=username)
            return redirect('/')
        else:
            print('Not User')
            messages.info(request, "Username or Password incorrect !")
            return render(request, 'home/login.html', )
    else:
        return render(request, 'home/login.html')


def logout_validate(request):
    logout(request)
    return redirect('home')


@login_required(login_url='/login')
def contact(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        number = request.POST['number']
        message = request.POST['message']
        time = datetime.datetime.now()

        if len(fname) < 2 or len(email) < 5 or len(number) < 10 or len(message) < 4:
            messages.error(request, "Please fill the form correctly !!!")
        else:
            contact = Contact(fname=fname, lname=lname, email=email, number=number, message=message, time=time)
            print(contact)
            contact.save()
            messages.success(request, "Your form has been submitted successfully.")
    return render(request, 'home/contact.html')


@login_required(login_url='/login')
def profile(request, id):
    member = Member.objects.get(user_id=id)
    return render(request, 'home/profile_page.html', {'member': member})


def test(request):
    return render(request, 'home/test.html')


@login_required(login_url='/login')
def allStudents(request):
    students = Member.objects.filter(Role='Student')
    return render(request, 'home/students_list.html', {'students': students})


@login_required(login_url='/login')
def allAlumni(request):
    alumni = Member.objects.filter(Role='Alumni')
    return render(request, 'home/alumni_list.html', {'alumni': alumni})


def EditProfile(request, id):
    member = Member.objects.get(user_id=id)
    form = EditProfileForm(instance=member)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'home/edit_profile.html', {'form': form})


def view_profile(request, id):
    member = Member.objects.get(user_id=id)
    return render(request, 'home/view_profile.html', {'member': member})