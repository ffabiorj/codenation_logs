from rest_framework.test import APIClient
from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
import json
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_401_UNAUTHORIZED,
    HTTP_400_BAD_REQUEST,
)


class PostLogTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        url = reverse("token")
        User.objects.create_user(
            username="teste", password="teste",
        )
        data = {"username": "teste", "password": "teste"}
        token = self.client.post(url, data=data, follow=True)

        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + token.data["access"])

    def test_post_status_code_201(self):
        data = {"log": "Test", "level": "warning", "event": 100}
        result = self.client.post(
            reverse("logs"), data=json.dumps(data), content_type="application/json"
        )
        assert result.status_code == HTTP_201_CREATED

    def test_post_status_code_401(self):
        self.client = APIClient(HTTP_AUTHORIZATION="")
        data = {"log": "Test", "level": "warning", "event": 100}
        result = self.client.post(
            reverse("logs"), data=json.dumps(data), content_type="application/json"
        )
        assert result.status_code == HTTP_401_UNAUTHORIZED

    def test_post_wrong_input_data(self):
        data = {"1": "1"}
        result = self.client.post(
            reverse("logs"), data=json.dumps(data), content_type="application/json"
        )
        assert result.status_code == HTTP_400_BAD_REQUEST
