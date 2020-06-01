from django.urls import path
from core import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("logs/", views.LogList.as_view(), name="logs"),
    path("log/<int:pk>/", views.LogDetail.as_view(), name="log"),
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
]
