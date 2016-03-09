from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from datetime import datetime
from quokka.models import Question, Answer, Votes, Set
from quokka.forms import AnswerForm

def index(request):
    question_list = Question.objects.all()
    answer_list = Answer.objects.all()
    votes_list = Votes.objects.all()
    context_dict = {'questions': question_list, 'answers': answer_list, 'votes': votes_list}
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
        	form.save(commit=True)
        	return index(request)
        else:
            print form.errors
    else:
        form = AnswerForm()
    return render(request, 'quokka/add_answer.html', {'form': form})