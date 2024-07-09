from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .serializers import UploadSerializer


class UploadViewSet(ViewSet):
    serializer_class = UploadSerializer

    def list(self, request):
        return Response("GET API")

    def create(self, request):
        file_uploaded = request.FILES.get('file_uploaded')
        content_type = file_uploaded.content_type
        response = "POST API and you have uploaded a {} file".format(content_type)
        return Response(response)

'''
def recruites(request):
    file = loader.get_template('home.html')
    return HttpResponse(file.render())
'''

def recruiter_home(request):
    file = loader.get_template('recruiter_home.html')
    return HttpResponse(file.render())


def recruiter_page(request):
    file = loader.get_template('recruiter_page.html')
    username = ['admin']
    context = {
        'username': username
    }
    return HttpResponse(file.render(context, request))
