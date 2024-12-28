from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.serializers import UserSerializer


class UserRetrieveAPIView(GenericAPIView):
    queryset = User.objects.none()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.request.user

    def get(self, request):
        serializer = self.get_serializer(instance=self.get_queryset())
        return Response(serializer.data, status=status.HTTP_200_OK)
