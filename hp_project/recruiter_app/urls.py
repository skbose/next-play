from django.urls import path, include
from . import views
from .views import UploadViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'upload', UploadViewSet, basename='upload')


urlpatterns = [
    path('recruiter_home/', views.recruiter_home, name='recruiter_home'),
    path('recruiter_page/', views.recruiter_page, name='recruiter_page'),
    path('upload/', include(router.urls)),
]
