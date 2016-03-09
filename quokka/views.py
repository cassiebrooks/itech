from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Quokka says hey there world!")

def about(request):
    return HttpResponse("Quokka tells you about itself!")
