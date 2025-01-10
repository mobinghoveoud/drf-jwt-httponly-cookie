from django.contrib.auth import authenticate
from django.middleware.csrf import rotate_token
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.jwt import set_token_cookies
from accounts.serializers import LoginSerializer


class LoginAPIView(APIView):
    serializer_class = LoginSerializer
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data["username"]
        password = serializer.validated_data["password"]
        user = authenticate(request, username=username, password=password)

        if not user:
            raise AuthenticationFailed

        response = Response({}, status=status.HTTP_200_OK)

        # Set auth cookies
        refresh = RefreshToken.for_user(user)
        set_token_cookies(response, str(refresh.access_token), str(refresh))

        # Rotate CSRF token
        # Django: For security reasons, CSRF tokens are rotated each time a user logs in.
        rotate_token(request)

        return response
