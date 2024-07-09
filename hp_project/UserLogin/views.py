from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def login_user(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        curr_path = request.POST['current_path']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if 'candidate' in curr_path:
                return redirect('candidate_page')
            else:
                return redirect('recruiter_page')
        else:
            messages.success(request, "There was as error loggin in, Try again...")
            return redirect('login')
    else:
        return render(request, 'authentication/login.html', {})
