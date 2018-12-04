import json

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.utils.safestring import mark_safe

from .models import Question


def splash(request):
    if request.method == "GET":
        return render(request, 'qa/splash.html')

    if request.method == "POST":
        sessionID = request.POST["sessionID"].lower()
        user = authenticate(username=sessionID, password="defaultuser")

        if user and user.is_active:
            request.session.set_expiry(5 * 60)
            login(request, user)
            return render(request, 'qa/voting.html')
        else:
            return render(request, 'qa/splash.html', {"error": "credentials"})


@login_required
def voting(request):
    if request.method == "GET":
        # list_of_appropriate_questions = sorted(list_of_appropriate_questions, key=lambda k: k['votes'], reverse=True)
        approved = [q.body for q in Question.objects.get(isAppropriate=True)]
        return render(request, 'qa/voting.html', {"questions": approved})

    if request.method == "POST":
        Question(body=request.POST["body"]).save()
        return render(request, 'qa/voting.html')


@login_required
def about(request):
    template = loader.get_template("qa/about.html")
    return HttpResponse(template.render())


########################################


@login_required
def index(request):
    return render(request, 'qa/index.html', {})


def room(request, room_name):
    return render(request, 'qa/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })

