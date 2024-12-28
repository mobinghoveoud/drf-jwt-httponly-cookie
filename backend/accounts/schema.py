from django.conf import settings
from drf_spectacular.contrib.rest_framework_simplejwt import SimpleJWTScheme
from drf_spectacular.utils import OpenApiParameter, _SerializerType
from drf_standardized_errors.openapi import AutoSchema
from rest_framework.permissions import SAFE_METHODS


class SimpleJWTCookieScheme(SimpleJWTScheme):
    target_class = "accounts.authentication.JWTCookieAuthentication"
    name = ["jwtHeaderAuth", "jwtCookieAuth"]

    def get_security_requirement(self, auto_schema):
        return [{name: []} for name in self.name]

    def get_security_definition(self, auto_schema):
        cookie_name = settings.SIMPLE_JWT["AUTH_COOKIE_ACCESS"]

        return [
            super().get_security_definition(auto_schema),
            {
                "type": "apiKey",
                "in": "cookie",
                "name": cookie_name,
            },
        ]


class CustomAutoSchema(AutoSchema):
    csrf_parameter = OpenApiParameter(
        name=settings.CSRF_HEADER_NAME.replace("HTTP_", "").replace("_", "-"),
        type=str,
        location=OpenApiParameter.HEADER,
        required=False,
        description="CSRF token",
    )

    def get_override_parameters(self) -> list[OpenApiParameter | _SerializerType]:
        params = super().get_override_parameters()

        if self.method not in SAFE_METHODS and bool(self.view.get_authenticators()):
            params.append(self.csrf_parameter)

        return params
