from django.urls import path
from . import views

urlpatterns = [
    path('candidate_login/login/', views.login_user, name="login"),
]
