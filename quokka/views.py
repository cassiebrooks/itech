from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from datetime import datetime
from quokka.models import Question, Answer, Vote, Set
from quokka.forms import AnswerForm

def index(request):
    question_list = Question.objects.all()
    answer_list = Answer.objects.all()
    vote_list = Vote.objects.all()
    context_dict = {'questions': question_list, 'answers': answer_list, 'votes': vote_list}
    response = render(request, 'quokka/index.html', context_dict)

    # Cookies
    visits = int(request.COOKIES.get('visits', '1'))
    reset_last_visit_time = False

    if 'last_visit' in request.COOKIES:
        last_visit = request.COOKIES['last_visit']
        last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")
        if (datetime.now() - last_visit_time).days > 0:
            visits = visits + 1
            reset_last_visit_time = True
    else:
        reset_last_visit_time = True
        context_dict['visits'] = visits
        response = render(request, 'quokka/index.html', context_dict)

    if reset_last_visit_time:
        response.set_cookie('last_visit', datetime.now())
        response.set_cookie('visits', visits)

    return response


def about(request):
	if request.session.get('visits'):
	    count = request.session.get('visits')
	else:
	    count = 0
	return render(request, 'quokka/about.html', {'visits': count})

@login_required
def add_answer(request):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            a = form.save(commit=False)
            a.author = request.user
            a.save()
            return index(request)
        else:
            print form.errors
    else:
        form = AnswerForm()
    return render(request, 'quokka/add_answer.html', {'form': form})

@login_required
def vote_on_answer(request):
    aid = None
    score = None
    if request.method == 'GET':
        aid = request.GET['answer_id']
        score = request.GET['score']

    if aid:
        a = Answer.objects.filter(id=int(aid)).first()
        if a:
            vote = Vote()
            vote.voter = request.user
            vote.answer = a
            vote.score = score
            vote.save()
    return HttpResponse(vote.score)

@login_required
def answer_question(request):
    if request.method == 'POST':
        #POST goes here . is_ajax is must to capture ajax requests. Beginner's pit.
        print "POST received"
        if request.is_ajax():
            #Always use get on request.POST. Correct way of querying a QueryDict.
            qid = request.POST['question_id']
            text = request.POST['text']

            print "QID and TEXT here"
            print qid
            print text

            q = Question.objects.filter(id=int(qid)).first()
            answer = Answer()
            answer.text = text
            answer.question = q
            answer.author = request.user
            answer.save()

            #data = (str) qid + "|" + (str) answer.id + "|" + text

            print "Data: " + data

            #Returning same data back to browser.It is not possible with Normal submit
            return HttpResponse(data)




    # qid = None
    # text = None
    # if request.method == 'POST':
    #     qid = request.GET['question_id']
    #     text = request.GET['text']

    # if qid:
    #     q = Question.objects.filter(id=int(qid)).first()
    #     if q:
    #         a.text = text
    #         a.question = q
    #         a.author = request.user
    #         a.save()
    # return HttpResponse(answer)

