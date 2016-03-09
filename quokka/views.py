from django.http import HttpResponse
from django.shortcuts import render
from quokka.models import Question, Answer, Votes, Set

def index(request):
    question_list = Question.objects.all()
    answer_list = Answer.objects.all()
    votes_list = Votes.objects.all()
    context_dict = {'questions': question_list, 'answers': answer_list, 'votes': votes_list}
    return render(request, 'quokka/index.html', context_dict)

def about(request):
    context_dict = {'boldmessage': "YAY QUOKKA"}
    return render(request, 'quokka/about.html', context_dict)
