from django.urls import path
from django.urls import path
from .views import register_user, login_user, logout_view

urlpatterns = [
    path('backend/register/', register_user, name='register'),
    path('backend/login/', login_user, name='login'),
    path('backend/logout/', logout_view, name='logout'),
]
