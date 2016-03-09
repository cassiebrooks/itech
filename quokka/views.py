from django.http import HttpResponse
from django.shortcuts import render
from quokka.models import Question, Answer, Votes, Set
from quokka.forms import AnswerForm

def index(request):
    question_list = Question.objects.all()
    answer_list = Answer.objects.all()
    votes_list = Votes.objects.all()
    context_dict = {'questions': question_list, 'answers': answer_list, 'votes': votes_list}
    return render(request, 'quokka/index.html', context_dict)

def about(request):
    context_dict = {'boldmessage': "YAY QUOKKA"}
    return render(request, 'quokka/about.html', context_dict)

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