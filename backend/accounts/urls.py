from django.urls import path

from accounts import views

app_name = "accounts"
urlpatterns = [
    # CSRF
    path("csrf_token/", views.CSRFAPIView.as_view(), name="csrf-token"),
    # Auth
    path("auth/refresh_token/", views.RefreshTokenAPIView.as_view(), name="refresh-token"),
    path("auth/login/", views.LoginAPIView.as_view(), name="login"),
    path("auth/logout/", views.LogoutAPIView.as_view(), name="logout"),
    # User
    path("user/", views.UserRetrieveAPIView.as_view(), name="user"),
]
