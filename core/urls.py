from django.urls import path
from core import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("log/", views.LogList.as_view(), name="log"),
    path("log/<int:pk>/", views.LogDetail.as_view(), name="log"),
    path("logs/", views.LogSearch.as_view(), name="search_logs"),
    path("token/", jwt_views.TokenObtainPairView.as_view(), name="token"),
    path("token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
]
