from django.contrib import messages
from django.shortcuts import render, redirect

from .models import *

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth.decorators import login_required


@login_required(login_url='/login')
def reunion(request):
    plan = Reunion.objects.order_by('Date')[::-1]
    user = request.user

    all_reunion = Paginator(Reunion.objects.order_by('Date')[::-1], 1)
    page = request.GET.get('page')
    try:
        plan = all_reunion.page(page)
    except PageNotAnInteger:
        plan = all_reunion.page(1)
    except EmptyPage:
        plan = all_reunion.page(all_reunion.num_pages)

    context = {'plan': plan, 'user': user}
    return render(request, 'connect/reunion.html', context)


@login_required(login_url='/login')
def add_reunion(request):
    if request.method == 'POST':
        title = request.POST['title']
        memo = request.POST['memo']
        place = request.POST['place']
        date = request.POST['date']
        batch = request.POST['batch']
        time = request.POST['time']
        user_ = request.user

        if len(title) < 5 or len(memo) < 25 or len(place) < 2 or len(batch) != 7:
            messages.error(request, "Please fill the form correctly !!!")

        else:
            form = Reunion(user=user_, Title=title, Memo=memo, Place=place, Date=date, Batch=batch, Time=time)
            form.save()
            messages.success(request, "Congrats !!! Your reunion has been created successfully.")

    return render(request, 'connect/add_reunion.html')


def participants_list(request):
    user = request.user

    if request.method == 'POST':
        reunion_id = request.POST.get('reunion_id')
        reunion_obj = Reunion.objects.get(Sr_No=reunion_id)

        if user in reunion_obj.Participants.all():
            reunion_obj.Participants.remove(user)
        else:
            reunion_obj.Participants.add(user)

        participant, created = List.objects.get_or_create(user=user, reunion_id=reunion_id)
        if not created:
            if participant.participants == "I'm In":
                participant.participants = "I'm Out"
            else:
                participant.participants = "I'm In"

        participant.save()

    return redirect('/connect/reunion')


def reunion_delete(request, reunion_id):
    reunion_ = Reunion.objects.filter(Sr_No=reunion_id)
    reunion_.delete()
    messages.info(request, 'Your Reunion has been successfully deleted.')
    return redirect('/connect/reunion')


@login_required(login_url='/login')
def webinar(request):
    user = request.user
    webinars = Webinar.objects.order_by('Date')[::-1]

    all_reunion = Paginator(Webinar.objects.order_by('Date')[::-1], 1)
    page = request.GET.get('page')
    try:
        webinars = all_reunion.page(page)
    except PageNotAnInteger:
        webinars = all_reunion.page(1)
    except EmptyPage:
        webinars = all_reunion.page(all_reunion.num_pages)

    context = {'user': user, 'webinars': webinars}
    return render(request, 'connect/webinar.html', context)


def webinar_delete(request, webinar_id):
    webinar_ = Webinar.objects.filter(Sr_No=webinar_id)
    webinar_.delete()
    messages.info(request, 'Your Webinar has been successfully deleted.')
    return redirect('/connect/webinar')


@login_required(login_url='/login')
def mentor(request):
    return render(request, 'connect/mentor.html')


def add_webinar(request):
    if request.method == 'POST':
        title = request.POST['title']
        memo = request.POST['memo']
        link = request.POST['link']
        date = request.POST['date']
        time = request.POST['time']
        user_ = request.user

        if len(title) < 5 or len(memo) < 20:
            messages.error(request, "Please fill the form correctly !!!")

        else:
            form = Webinar(user=user_, Title=title, Memo=memo, Link=link, Date=date, Time=time)
            form.save()
            messages.success(request, "Congrats !!! Your webinar has been created successfully.")

    return render(request, 'connect/add_webinar.html')


def add_achievement(request):
    if request.POST:
        user = request.user
        detail = request.POST['detail']
        form = Achievement(user=user, Memo=detail)
        form.save()
        return redirect('/')
    return render(request, '/home/home.html')


def p_list(request, id):
    organizer = Reunion.objects.get(Sr_No=id)
    all = organizer.Participants.all()
    print(all)
    return render(request, 'connect/reunion.html', {'all': all})
