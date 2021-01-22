from django.contrib import messages
from django.shortcuts import render, redirect
# this is my comment
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime

from .decorators import unauthenticated_user
from .forms import CreateUserForm, EditProfileForm, RoleAddFrom
from .models import *
from connect.models import Achievement
from .filters import MemberFilter


def home(request):
    achievements = Achievement.objects.filter(visible='Show')
    context = {'achievements': achievements}
    return render(request, 'home/home.html', context)


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

            contact.save()
            messages.success(request, "Your form has been submitted successfully.")
    return render(request, 'home/contact.html')


@login_required(login_url='/login')
def profile(request, id):
    member = Member.objects.get(user_id=id)
    form = EditProfileForm(instance=member)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            return redirect('/profile/' + str(id))
    return render(request, 'home/profile_page.html', {'member': member, 'form': form})


def test(request):
    return render(request, 'home/test.html')


@login_required(login_url='/login')
def allAlumni(request):
    alumni = Member.objects.filter(Role='Alumni')
    filter_form = MemberFilter(request.GET, queryset=alumni)
    alumni = filter_form.qs
    return render(request, 'home/alumni_list.html', {'alumni': alumni, 'filter_form': filter_form})


def search_alumni(request):
    query = request.GET['query']

    if len(query) > 50:
        alumni = Member.objects.none()

    else:
        alumni_role = Member.objects.filter(Role__icontains='Alumni')
        alumni_fname = Member.objects.filter(user__first_name__icontains=query)
        alumni_lname = Member.objects.filter(user__last_name__icontains=query)

        alumni = alumni_role & (alumni_fname | alumni_lname)

    context = {'alumni': alumni, 'query': query}
    return render(request, 'home/search_alumni.html', context)


@login_required(login_url='/login')
def allStudents(request):
    students = Member.objects.filter(Role='Student')
    filter_form = MemberFilter(request.GET, queryset=students)
    students = filter_form.qs
    return render(request, 'home/students_list.html', {'students': students, 'filter_form': filter_form})


def search_student(request):
    query = request.GET['query']

    if len(query) > 50:
        students = Member.objects.none()

    else:
        student_role = Member.objects.filter(Role__icontains='Student')
        student_fname = Member.objects.filter(user__first_name__icontains=query)
        student_lname = Member.objects.filter(user__last_name__icontains=query)

        students = student_role & (student_fname | student_lname)

    context = {'students': students, 'query': query}
    return render(request, 'home/search_student.html', context)


def view_profile(request, id):
    member = Member.objects.get(user_id=id)
    return render(request, 'home/view_profile.html', {'member': member})


'''
def filter(request, role, branch):
    if role == 'alumni':
        if branch == 'cs':
            alumni = Member.objects.filter(Role='Alumni',Branch='Computer Science')
        elif branch == 'mech':
            alumni = Member.objects.filter(Role='Alumni', Branch='Mechanical Engineering')
        elif branch == 'entc':
            alumni = Member.objects.filter(Role='Alumni', Branch='Electronics & Telecommunication')
        elif branch == 'chem':
            alumni = Member.objects.filter(Role='Alumni', Branch='Chemical Engineering')
        elif branch == 'civ':
            alumni = Member.objects.filter(Role='Alumni', Branch='Civil Engineering')
        else:
            alumni = Member.objects.filter(Role='Alumni', Branch='Others')

        return render(request, 'home/alumni_list.html', {'alumni': alumni})

    if role == 'student':
        if branch == 'cs':
            student = Member.objects.filter(Role='Student',Branch='Computer Science')
        elif branch == 'mech':
            student = Member.objects.filter(Role='Student', Branch='Mechanical Engineering')
        elif branch == 'entc':
            student = Member.objects.filter(Role='Student', Branch='Electronics & Telecommunication')
        elif branch == 'chem':
            student = Member.objects.filter(Role='Student', Branch='Chemical Engineering')
        elif branch == 'civ':
            student = Member.objects.filter(Role='Student', Branch='Civil Engineering')
        else:
            student = Member.objects.filter(Role='Student', Branch='Others')

        return render(request, 'home/students_list.html', {'students': student})

'''
