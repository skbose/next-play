from django.contrib.auth.backends import ModelBackend
from authentication.models import User

class UserIDBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(user_id=username)  # Use `user_id` for authentication
        except User.DoesNotExist:
            return None
        
        if user.check_password(password):  # Check the hashed password
            return user
        return None
