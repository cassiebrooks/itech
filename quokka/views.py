from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render(request, 'quokka/index.html', context_dict)

def about(request):
    context_dict = {'boldmessage': "YAY QUOKKA"}
    return render(request, 'quokka/about.html', context_dict)
