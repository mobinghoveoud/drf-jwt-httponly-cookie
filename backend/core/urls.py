from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
]

if settings.DEBUG:
    urlpatterns += [
        # OpenAPI UI
        path("schema/", SpectacularAPIView.as_view(), name="schema"),
        path("schema/swagger-ui/", SpectacularSwaggerView.as_view(), name="swagger-ui"),
        path("schema/redoc/", SpectacularRedocView.as_view(), name="redoc"),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
