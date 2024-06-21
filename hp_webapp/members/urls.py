from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
    path('candidate/', views.candidate, name='candidate'),
    path('recruiter/', views.recruiter, name='recruiter'),
    path('candidate/login/', views.login, name='login'),
    path('recruiter/login/', views.login, name='login'),
    #path('logout/', views.logout_view, name='logout'),
]
