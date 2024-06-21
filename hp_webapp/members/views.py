from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers':mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymembers = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('template.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def candidate(request):
    template = loader.get_template('candidate.html')
    return HttpResponse(template.render())

def recruiter(request):
    template = loader.get_template('recruiter.html')
    return HttpResponse(template.render())

def login(request):

    template = loader.get_template('login.html')
    return HttpResponse(template.render())
    '''
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('HOME')
    else:
        form = AuthenticationForm()
    return render(request, 'members/login.html', {'form':form})
    '''

def logout_view(request):
    logout(request)
    return redirect('login')
