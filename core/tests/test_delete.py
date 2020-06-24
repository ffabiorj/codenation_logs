from rest_framework.test import APIClient
from core.models import Log
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.status import (
    HTTP_401_UNAUTHORIZED,
    HTTP_204_NO_CONTENT,
    HTTP_404_NOT_FOUND,
)


class DeleteLogTest(TestCase):
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

    def test_delete_log_by_id(self):
        expect = self.client.delete(reverse("log", kwargs={"pk": self.log.pk}))

        assert expect.status_code == HTTP_204_NO_CONTENT

    def test_delete_unauthorized_log(self):
        self.client = APIClient(HTTP_AUTHORIZATION="")
        result = self.client.delete(reverse("log", kwargs={"pk": 1}))
        assert result.status_code == HTTP_401_UNAUTHORIZED

    def test_delete_non_existent_id(self):
        result = self.client.delete(reverse("log", kwargs={"pk": 30}))
        assert result.status_code == HTTP_404_NOT_FOUND
