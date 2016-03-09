from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render(request, 'quokka/index.html', context_dict)

def about(request):
    return HttpResponse("Quokka tells you about itself!")
