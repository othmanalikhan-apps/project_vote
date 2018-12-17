import json
from builtins import enumerate

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponseRedirect
from django.shortcuts import render

from vote.settings import LOGIN_PASSWORD
from .models import Question


def splash(request):
    if request.method == "GET":
        return render(request, 'qa/splash.html')

    if request.method == "POST":
        sessionID = request.POST["sessionID"]
        user = authenticate(username=sessionID, password=LOGIN_PASSWORD)

        if user and user.is_active:
            request.session.set_expiry(15 * 60)
            login(request, user)
            return HttpResponseRedirect("/voting")
        else:
            return render(request, 'qa/splash.html', {"error": "credentials"})


@login_required
def voting(request):
    if request.method == "GET":
        approved = []
        qs = Question.objects.filter(isAppropriate=True).order_by("-votes")
        qs = serializers.serialize("json", qs)
        qs = [entry["fields"] for entry in json.loads(qs)]
        qs = qs[:40]

        for i, entry in enumerate(qs, start=1):
            entry.pop("isAppropriate")
            entry["num"] = i
            approved.append(entry)

        return render(request, 'qa/voting.html', {"questions": approved})

    if request.method == "POST":
        if request.POST["body"]:
            Question(body=request.POST["body"]).save()
            msg = "Submitted your question to the server successfully!"
            messages.success(request, msg)
            return HttpResponseRedirect("/voting")
        else:
            return HttpResponseRedirect("/voting")


@login_required
def about(request):
    return render(request, 'qa/about.html')


def stress(request):
    """
    Points to a file required for stress testing via loader.io website.
    """
    return render(request, 'qa/loaderio.html')
