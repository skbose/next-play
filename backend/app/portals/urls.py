from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('create-job/', views.create_job, name='create_job'),
    path('apply-job/<int:job_id>/', views.apply_to_job, name='apply_to_job'),
    path('job/<str:unique_link>/', views.get_job_by_link, name='get_job_by_link'),
    path('recruiter/jobs/', views.list_recruiter_jobs, name='list_recruiter_jobs'),
    path('jobs/', views.list_jobs, name='list_jobs'),
    path('recruiter/applications/', views.list_applications, name='list_applications'),
    
] 

# Serve media files during development
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
