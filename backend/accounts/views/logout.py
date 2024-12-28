from django.conf import settings
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.serializers import TokenBlacklistSerializer
from rest_framework_simplejwt.tokens import Token

from accounts.jwt import delete_token_cookies


@extend_schema(request=None)
class LogoutAPIView(APIView):
    serializer_class = TokenBlacklistSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(data={"refresh": self.get_refresh_token_from_cookie()})

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0]) from e

        response = Response({}, status=status.HTTP_200_OK)

        # Delete jwt cookies
        delete_token_cookies(response)

        return response

    def get_refresh_token_from_cookie(self) -> Token:
        refresh = self.request.COOKIES.get(settings.SIMPLE_JWT["AUTH_COOKIE_REFRESH"])
        print(refresh)
        if not refresh:
            raise PermissionDenied

        return refresh
