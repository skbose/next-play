from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from .serializers import UploadSerializer
from django.conf import settings
import os


class UploadViewSet(ViewSet):
    serializer_class = UploadSerializer

    def create(self, request):
        file_uploaded = request.FILES.get('file')
        if not file_uploaded:
            return Response({"error": "No file uploaded"}, status=status.HTTP_400_BAD_REQUEST)

        content_type = file_uploaded.content_type
        if content_type != 'application/pdf':
            return Response({"error": "Only PDF files are allowed"}, status=status.HTTP_400_BAD_REQUEST)

        file_path = os.path.join(settings.MEDIA_ROOT, file_uploaded.name)
        with open(file_path, 'wb+') as destination:
            for chunk in file_uploaded.chunks():
                destination.write(chunk)

        context = {'file_name': file_uploaded.name, 'content_type': content_type, 'success': True}
        template = loader.get_template('recruiter_upload.html')
        return HttpResponse(template.render(context, request))

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


def recruiter_upload(request):
    template = loader.get_template('recruiter_upload.html')
    context = {}
    return HttpResponse(template.render(context, request))


def upload_list(request):
    upload_dir = settings.MEDIA_ROOT
    files = os.listdir(upload_dir)
    files = [file for file in files if os.path.isfile(os.path.join(upload_dir, file))]
    context = {'files': files}
    template = loader.get_template('upload_list.html')
    return HttpResponse(template.render(context, request))
