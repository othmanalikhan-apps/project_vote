import json

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.utils.safestring import mark_safe
from django.core import serializers

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
            return HttpResponseRedirect("/voting")
        else:
            return render(request, 'qa/splash.html', {"error": "credentials"})


@login_required
def voting(request):
    if request.method == "GET":
        approved = Question.objects.filter(isAppropriate=True).order_by("-votes")
        approved = serializers.serialize("json", approved)
        approved = [entry["fields"] for entry in json.loads(approved)]
        approved = approved[:20]
        return render(request, 'qa/voting.html', {"questions": approved})

    if request.method == "POST":
        if request.POST["body"]:
            Question(body=request.POST["body"]).save()
            messages.success(request, "success")
            return HttpResponseRedirect("/voting")
        else:
            return HttpResponseRedirect("/voting")


@login_required
def about(request):
    template = loader.get_template("qa/about.html")
    return HttpResponse(template.render())


######################################## DJANGO CHANNELS


def index(request):
    return render(request, 'qa/index.html', {})


def room(request, room_name):
    return render(request, 'qa/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })
