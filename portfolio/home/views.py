from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('This is my homepage')

def resume(request):
    return HttpResponse('This is my resume page')

def projects(request):
    return HttpResponse('This is my projects page')

def services(request):
    return HttpResponse(' This is my servicepage')

def contact(request):
    return HttpResponse('This is my contactpage')