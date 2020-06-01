from django.urls import path
from core import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("logs/", views.LogList.as_view(), name="logs"),
    path("log/<int:pk>/", views.LogDetail.as_view(), name="log"),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
