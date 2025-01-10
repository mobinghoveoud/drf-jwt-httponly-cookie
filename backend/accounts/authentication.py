from django.conf import settings
from rest_framework.authentication import CSRFCheck
from rest_framework.exceptions import PermissionDenied
from rest_framework_simplejwt.authentication import JWTAuthentication


class CSRFPermissionDeniedError(PermissionDenied):
    default_code = "csrf_permission_denied"


class JWTCookieAuthentication(JWTAuthentication):
    def authenticate(self, request):
        header = self.get_header(request)

        if header is None:
            raw_token = request.COOKIES.get(settings.SIMPLE_JWT["AUTH_COOKIE_ACCESS"]) or None
        else:
            raw_token = self.get_raw_token(header)

        if raw_token is None:
            return None

        if settings.SIMPLE_JWT["AUTH_COOKIE_USE_CSRF"]:
            self.enforce_csrf(request)

        validated_token = self.get_validated_token(raw_token)

        return self.get_user(validated_token), validated_token

    def enforce_csrf(self, request):
        def dummy_get_response(_):
            return None

        check = CSRFCheck(dummy_get_response)
        # populates request.META['CSRF_COOKIE'], which is used in process_view()
        check.process_request(request)
        reason = check.process_view(request, None, (), {})
        if reason:
            raise CSRFPermissionDeniedError(f"CSRF Failed: {reason}")
