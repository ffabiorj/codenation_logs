from django.urls import path
from core import views

urlpatterns = [
    path('logs/', views.LogList.as_view(), name='logs')
]
