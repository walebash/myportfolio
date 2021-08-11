from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home/home_page.html', {})

def about(request):
    return render(request, 'home/about.html', {})

def projects(request):
    return render(request, 'home/projects.html', {})

def contact(request):
    context1 = {
        'My_email' : 'Email : bashiradigun78@gmail.com',
        'Mobile_number' : 'Mobile number: +23480777777777'
    }
    return render(request, 'home/contact.html', context1)

def blog(request):
    return render(request, 'home/blog.html', {})

# def register(request):
#     return render(request, 'home/register.html', {})