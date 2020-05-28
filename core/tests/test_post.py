from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from django.urls import reverse
import pytest
from django.contrib.auth.models import User
import json
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_401_UNAUTHORIZED,
    HTTP_400_BAD_REQUEST,
)


@pytest.mark.django_db
def test_post_status_code_201():
    user = User.objects.create_user(username="Fabio", password="test",)
    token, created = Token.objects.get_or_create(user=user)
    client = APIClient(HTTP_AUTHORIZATION="Token " + token.key)
    data = {"log": "Test"}
    result = client.post(
        reverse("logs"), data=json.dumps(data), content_type="application/json"
    )
    assert result.status_code == HTTP_201_CREATED


def test_post_status_code_401():
    client = APIClient(HTTP_AUTHORIZATION="")
    data = {"log": "Test"}
    result = client.post(
        reverse("logs"), data=json.dumps(data), content_type="application/json"
    )
    assert result.status_code == HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_post_wrong_input_data():
    user = User.objects.create_user(username="Fabio", password="test",)
    token, created = Token.objects.get_or_create(user=user)
    client = APIClient(HTTP_AUTHORIZATION="Token " + token.key)
    data = {"1": "1"}
    result = client.post(
        reverse("logs"), data=json.dumps(data), content_type="application/json"
    )
    assert result.status_code == HTTP_400_BAD_REQUEST
