from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def candidates(request):
    file = loader.get_template('home.html')
    return HttpResponse(file.render())

def candidate_login(request):
    file = loader.get_template('candidate_home.html')
    return HttpResponse(file.render())
