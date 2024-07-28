from django.urls import path, include
from . import views
from .views import UploadViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'upload', UploadViewSet, basename='upload')

urlpatterns = [
    path('', views.candidates, name='candidates'),
    path('candidate_home/', views.candidate_home, name='candidate_home'),
    path('candidate_page/', views.candidate_page, name='candidate_page'),
    path('candidate_page/upload/', views.candidate_upload, name='candidate_upload'),
    path('candidate_page/upload/list/', views.upload_list, name='upload_list'),
    path('api/', include(router.urls)),
]
