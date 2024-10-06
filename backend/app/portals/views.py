# views.py
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Job, JobApplication
from .serializers import JobSerializer, JobApplicationSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

# Create Job (Recruiter)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_job(request):
    print(request)
    serializer = JobSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        job = serializer.save(recruiter=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Apply to Job (Candidate)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def apply_to_job(request, job_id):
    try:
        job = Job.objects.get(id=job_id)
    except Job.DoesNotExist:
        return Response({'error': 'Job not found'}, status=status.HTTP_404_NOT_FOUND)

    data = request.data
    data['job'] = job.id
    data['candidate'] = request.user.id
    data['experience_summary'] = request.data.get('experience_summary', '')
    data['email_id'] = request.data.get('email_id', '')
    data['contact_no'] = request.data.get('contact_no', '')

    serializer = JobApplicationSerializer(data=data, context={'request': request})

    if serializer.is_valid():
        serializer.save(candidate=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# List All Jobs (Anyone can view)
@api_view(['GET'])
def list_jobs(request):
    jobs = Job.objects.all()
    serializer = JobSerializer(jobs, many=True, context={'request': request})
    return Response(serializer.data)

# List Jobs of a Recruiter
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_recruiter_jobs(request):
    jobs = Job.objects.filter(recruiter=request.user)
    serializer = JobSerializer(jobs, many=True, context={'request': request})
    return Response(serializer.data)

# List Applications for a Recruiter
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_applications(request):
    jobs = Job.objects.filter(recruiter=request.user)
    applications = JobApplication.objects.filter(job__in=jobs)
    serializer = JobApplicationSerializer(applications, many=True, context={'request': request})
    return Response(serializer.data)

# Get Job by Unique Link
@api_view(['GET'])
def get_job_by_link(request, unique_link):
    try:
        job = Job.objects.get(unique_link=unique_link)
    except Job.DoesNotExist:
        return Response({'error': 'Job not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = JobSerializer(job, context={'request': request})
    return Response(serializer.data)
