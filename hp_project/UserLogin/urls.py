from django.urls import path
from . import views

urlpatterns = [
    path('candidate_home/login/', views.login_user, name="login"),
    path('recruiter_home/login/', views.login_user, name="login"),
]
