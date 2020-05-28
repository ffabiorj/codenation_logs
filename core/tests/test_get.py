from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from django.urls import reverse
import pytest
from django.contrib.auth.models import User
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_get_status_code_200():
    user = User.objects.create_user(username="Fabio", password="test",)
    token, created = Token.objects.get_or_create(user=user)
    client = APIClient(HTTP_AUTHORIZATION="Token " + token.key)
    result = client.get(reverse("logs"))
    assert result.status_code == HTTP_200_OK


def test_get_status_code_401():
    client = APIClient(HTTP_AUTHORIZATION="")
    result = client.get(reverse("logs"))
    assert result.status_code == HTTP_401_UNAUTHORIZED


def test_get_message_error():
    client = APIClient(HTTP_AUTHORIZATION="")
    result = client.get(reverse("logs"))
    expected = {"detail": "Authentication credentials were not provided."}
    assert result.json() == expected
