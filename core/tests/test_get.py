from rest_framework.test import APIClient
from django.urls import reverse
from core.models import Log
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND


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

    def test_get_status_code_200(self):
        result = self.client.get(reverse("logs"))
        assert result.status_code == HTTP_200_OK

    def test_get_status_code_401(self):
        self.client = APIClient(HTTP_AUTHORIZATION="")
        result = self.client.get(reverse("logs"))
        assert result.status_code == HTTP_401_UNAUTHORIZED

    def test_get_message_error(self):
        self.client = APIClient(HTTP_AUTHORIZATION="")
        result = self.client.get(reverse("logs"))
        expected = {"detail": "Authentication credentials were not provided."}
        assert result.json() == expected

    def test_get_log_by_id(self):
        result = self.client.get(reverse("log", kwargs={"pk": self.log.pk}))
        assert result.status_code == HTTP_200_OK

    def test_get_log_by_non_existent_id(self):
        result = self.client.get(reverse("log", kwargs={"pk": 30}))
        assert result.status_code == HTTP_404_NOT_FOUND

    def test_get_log_by_id_unauthorized(self):
        self.client = APIClient(HTTP_AUTHORIZATION="")
        result = self.client.get(reverse("log", kwargs={"pk": 1}))
        assert result.status_code == HTTP_401_UNAUTHORIZED
