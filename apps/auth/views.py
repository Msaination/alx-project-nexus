from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.serializers import RegisterSerializer

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    """
    Register a new user with password + confirm password.
    """
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class LoginView(TokenObtainPairView):
    """
    Login user and return JWT access + refresh tokens.
    """
    # You can override serializer if you want custom claims


class RefreshView(TokenRefreshView):
    """
    Refresh JWT access token using refresh token.
    """


class LogoutView(APIView):
    """
    Logout user by blacklisting their refresh token.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)
        except Exception:
            return Response({"detail": "Invalid refresh token."}, status=status.HTTP_400_BAD_REQUEST)


