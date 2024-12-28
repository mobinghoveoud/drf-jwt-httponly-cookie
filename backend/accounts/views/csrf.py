from django.middleware.csrf import get_token
from drf_spectacular.utils import extend_schema, inline_serializer
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView


@extend_schema(request=None, responses=inline_serializer("CSRFSerializer", {"token": serializers.CharField()}))
class CSRFAPIView(APIView):
    permission_classes = ()
    authentication_classes = ()

    def get(self, request):
        return Response({"token": get_token(request)})
