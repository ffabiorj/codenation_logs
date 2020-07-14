from rest_framework.test import APIClient
from django.urls import reverse
from core.models import Log
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_401_UNAUTHORIZED,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
)


class GetLogTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        url = reverse("token")
        self.log = Log.objects.create(log="Teste", level="warning", event=100)
        User.objects.create_user(
            username="teste", password="teste",
        )
        data = {"username": "teste", "password": "teste"}
        token = self.client.post(url, data=data, follow=True)

        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + token.data["access"])

    def test_put_log_status_ok(self):
        data = {"log": "Teste", "level": "warning", "event": 1000, "archived": True}
        result = self.client.put(reverse("log", kwargs={"pk": self.log.pk}), data=data)
        assert result.status_code == HTTP_200_OK

    def test_put_log_bad_request(self):
        data = {}
        result = self.client.put(reverse("log", kwargs={"pk": self.log.pk}), data=data)
        assert result.status_code == HTTP_400_BAD_REQUEST

    def test_put_log_by_non_existent_id(self):
        data = {"log": "Teste", "level": "warning", "event": 1000, "archived": True}
        result = self.client.put(reverse("log", kwargs={"pk": 30}), data=data)
        assert result.status_code == HTTP_404_NOT_FOUND

    def test_put_log_by_id_unauthorized(self):
        self.client = APIClient(HTTP_AUTHORIZATION="")
        data = {"log": "Teste", "level": "warning", "event": 1000, "archived": True}
        result = self.client.put(reverse("log", kwargs={"pk": 1}), data=data)
        assert result.status_code == HTTP_401_UNAUTHORIZED
