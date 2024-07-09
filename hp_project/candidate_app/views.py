from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .serializers import UploadSerializer


class UploadViewSet(ViewSet):
    serializer_class = UploadSerializer

    '''def list(self, request):
        #return Response("GET API")
        file = loader.get_template('upload_success.html')
        return Response(file.render())'''

    def create(self, request):
        file_uploaded = request.FILES.get('file_uploaded')
        content_type = file_uploaded.content_type
        response = "POST API and you have uploaded a {} file".format(content_type)
        file = loader.get_template('upload_success.html')
        #return Response(file.render())
        return Response(response)


def candidates(request):
    file = loader.get_template('home.html')
    return HttpResponse(file.render())


def candidate_home(request):
    file = loader.get_template('candidate_home.html')
    return HttpResponse(file.render())


def candidate_page(request):
    file = loader.get_template('candidate_page.html')
    username = ['admin']
    context = {
        'username': username
    }
    return HttpResponse(file.render(context, request))