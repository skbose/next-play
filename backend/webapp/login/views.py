from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.decorators import api_view


@api_view(['GET'])
def login(request):
    return render(request, 'login/index.html')


@api_view(['POST'])
def authenticate(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    # if user_type == "candidate":
    #     return render(request, 'profile/candidate.html')
    # elif user_type == "recruiter":
    #     return render(request, 'profile/recruiter.html')
    # else:
    #     return render(request, 'profile/404.html')