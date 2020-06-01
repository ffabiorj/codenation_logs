from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from core.models import Log
from django.urls import reverse
import pytest
from django.contrib.auth.models import User
from rest_framework.status import (
    HTTP_401_UNAUTHORIZED,
    HTTP_204_NO_CONTENT,
    HTTP_404_NOT_FOUND,
)


@pytest.mark.django_db
def test_delete_log_by_id():
    log = Log.objects.create(log="Teste", level="warning", event=100)
    user = User.objects.create_user(username="Fabio", password="test",)
    token, created = Token.objects.get_or_create(user=user)
    client = APIClient(HTTP_AUTHORIZATION="Token " + token.key)
    result = client.delete(reverse("log", kwargs={"pk": log.pk}))
    assert result.status_code == HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_delete_unauthorized_log():
    client = APIClient(HTTP_AUTHORIZATION="")
    result = client.delete(reverse("log", kwargs={"pk": 1}))
    assert result.status_code == HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_delete_non_existent_id():
    user = User.objects.create_user(username="Fabio", password="test",)
    token, created = Token.objects.get_or_create(user=user)
    client = APIClient(HTTP_AUTHORIZATION="Token " + token.key)
    result = client.delete(reverse("log", kwargs={"pk": 30}))
    assert result.status_code == HTTP_404_NOT_FOUND
