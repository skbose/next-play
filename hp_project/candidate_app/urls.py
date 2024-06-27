from django.urls import path
from . import views

urlpatterns = [
    path('', views.candidates, name='candidates'),
    path('candidate_login/', views.candidate_login, name='candidate_login'),
]
