from django.contrib import messages
from django.shortcuts import render, redirect

from .models import *

from django.contrib.auth.decorators import login_required


@login_required(login_url='/login')
def reunion(request):
    plan = Reunion.objects.order_by('Date')[::-1]
    user = request.user
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


@login_required(login_url='/login')
def mentor(request):
    return render(request, 'connect/mentor.html')


@login_required(login_url='/login')
def webinar(request):
    user = request.user
    webinars = Webinar.objects.all()
    context = { 'user': user, 'webinars': webinars }
    return render(request, 'connect/webinar.html',context)


