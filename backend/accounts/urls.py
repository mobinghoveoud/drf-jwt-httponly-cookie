from django.urls import path

from accounts import views

app_name = "accounts"
urlpatterns = [
    # Auth
    path("auth/refresh_token/", views.RefreshTokenAPIView.as_view(), name="refresh-token"),
    path("auth/login/", views.LoginAPIView.as_view(), name="login"),
    # User
    path("user/", views.UserRetrieveAPIView.as_view(), name="user"),
]
