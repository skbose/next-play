from django.urls import path, include
from . import views
from .views import UploadViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', UploadViewSet, basename='')


urlpatterns = [
    path('', views.candidates, name='candidates'),
    path('candidate_home/', views.candidate_home, name='candidate_home'),
    path('candidate_page/', views.candidate_page, name='candidate_page'),
    path('candidate_page/upload/', include(router.urls)),
]
