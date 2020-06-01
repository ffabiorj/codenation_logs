from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from django.urls import reverse
from core.models import Log
import pytest
from django.contrib.auth.models import User
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND


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


@pytest.mark.django_db
def test_get_log_by_id():
    log = Log.objects.create(log="Teste", level="warning", event=100)
    user = User.objects.create_user(username="Fabio", password="test",)
    token, created = Token.objects.get_or_create(user=user)
    client = APIClient(HTTP_AUTHORIZATION="Token " + token.key)
    result = client.get(reverse("log", kwargs={"pk": log.pk}))
    assert result.status_code == HTTP_200_OK


@pytest.mark.django_db
def test_get_log_by_non_existent_id():
    user = User.objects.create_user(username="Fabio", password="test",)
    token, created = Token.objects.get_or_create(user=user)
    client = APIClient(HTTP_AUTHORIZATION="Token " + token.key)
    result = client.get(reverse("log", kwargs={"pk": 30}))
    assert result.status_code == HTTP_404_NOT_FOUND


def test_get_log_by_id_unauthorized():
    client = APIClient(HTTP_AUTHORIZATION="")
    result = client.get(reverse("log", kwargs={"pk": 1}))
    assert result.status_code == HTTP_401_UNAUTHORIZED
