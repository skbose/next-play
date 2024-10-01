from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .serializers import UserSerializer
from django.contrib.auth import authenticate

# Registration API
@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        user.set_password(request.data.get("password"))
        user.save()
        return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Login API (Token-based login)
@api_view(['POST'])
def login_user(request):
    user_id = request.data.get('user_id')
    password = request.data.get('password')
    user = authenticate(user_id=user_id, password=password)

    if user is not None:
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user_type': user.user_type,
            'user_id': user.user_id,
            'username': user.name
        })
    else:
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logging out