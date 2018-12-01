import json
from django.template import RequestContext

from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.utils.safestring import mark_safe

from .models import Question


def splash(request):
    if request.method == "GET":
        return render(request, 'qa/splash.html', {})

    if request.method == "POST":
        sessionID = request.POST["sessionID"]
        user = authenticate(username=sessionID, password="defaultuser")

        if user and user.is_active:
            request.session.set_expiry(5*60)
            login(request, user)
            template = loader.get_template("qa/questions.html")

            # print(request)
            # print(rd)
            # return HttpResponse(template.render(request))
            return render(request, 'qa/questions.html')


########################################


@login_required
def index(request):
    return render(request, 'qa/index.html', {})


def room(request, room_name):
    return render(request, 'qa/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })


########################################

@login_required
def questions(request):
    template = loader.get_template("qa/questions.html")
    return HttpResponse(template.render())

    # if request.method == 'GET':
    #     r = requests.get(BACKEND_URL + "questions/")
    #     # I am trying to store the json in a string variable
    #     s = json.dumps(r.json(), indent=4)
    #     list_of_questions = r.json()
    #     for question in list_of_questions:
    #         question["ajaxId"] = "ajaxId" + str(question["id"])
    #
    #     # Filtering inappropriate questions
    #     list_of_appropriate_questions = [question for question in list_of_questions if question["isAppropriate"]]
    #     list_of_appropriate_questions = sorted(list_of_appropriate_questions, key=lambda k: k['votes'], reverse=True)
    #
    #     context = {
    #         'questions': list_of_appropriate_questions,
    #     }
    #
    #     return HttpResponse(template.render(context, request))
    # return HttpResponseRedirect('QA')


@login_required
def about(request):
    template = loader.get_template("qa/about.html")
    return HttpResponse(template.render())


def new_question(request):
    print("FSDKLSDKLFSDLKFSDKJ")
    if request.method == "POST":
        Question(body=request.POST["body"]).save()
        # return HttpResponseRedirect("/questions")
        template = loader.get_template("qa/questions.html")
        # return HttpResponse(template.render())
        context = {}
        return render(request, 'qa/questions.html', context)

    # return render(request, 'qa/splash.html', {})

    # template = loader.get_template("qa/questions.html")
    # return HttpResponseRedirect("/questions")
    # return HttpResponse(template.render(), RequestContext(request))
    # return render(request, "qa/questions.html")


# def create_question(request):
#     form = NewQuestionForm(data=request.POST)
#     if form.is_valid():
#         #print("Form is valid")
#         # if True:
#         # Creates an object from the form. Doesn't save it though!
#         qa = form.save(commit=False)
#         # Getting data that is formatted properly so we can pass it to the API/database
#         question = form.cleaned_data['body']
#         #print("Create_question is called")
#         # This gets you the stuff.. Now we need to put them in a json file and send them to the API
#         dic = {"body": question}
#         # iles = {"image": open(request.FILES['myfile'], 'rb')}
#
#         r = requests.post(BACKEND_URL + 'questions/', data=dic)
#     return HttpResponseRedirect('QA')
#
#
# def question_voting(request):
#     try:
#         print("Is this my IP? {}".format(request.environ['REMOTE_ADDR']))
#         message = {"votes" : dict(request.POST)["checkbox"], "ip_address": request.environ['REMOTE_ADDR']}
#         r = requests.post(BACKEND_URL + 'vote/', data=message)
#         return HttpResponseRedirect('QA')
#     except:
#         return HttpResponseRedirect('QA')
#
#
# def vote_count_ajax(request, pk):
#     if request.method == 'GET':
#         r = requests.get(BACKEND_URL + "vote_count_ajax/" + str(pk))
#         return HttpResponse(r, content_type="application/xml")
#
#
# def vote_count_ajax_all(request):
#     if request.method == 'GET':
#         r = requests.get(BACKEND_URL + "vote_count_ajax_all/")
#         return HttpResponse(r, content_type="application/json")
#
#
# def question_count(request):
#     if request.method == 'GET':
#         r = requests.get(BACKEND_URL + "question_count")
#         return HttpResponse(r, content_type="application/xml")
