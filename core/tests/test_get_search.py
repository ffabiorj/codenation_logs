from rest_framework.test import APIClient
from django.urls import reverse
from core.models import Log
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED


class SearchLogTest(TestCase):
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

    def test_get_first_result(self):
        result = self.client.get(reverse("search_logs"))
        expect = result.json()["results"][0]["log"]
        assert expect == "Teste"

    def test_get_status_code_200(self):
        result = self.client.get(reverse("search_logs"))
        assert result.status_code == HTTP_200_OK

    def test_get_status_code_401(self):
        self.client = APIClient(HTTP_AUTHORIZATION="")
        result = self.client.get(reverse("search_logs"))
        assert result.status_code == HTTP_401_UNAUTHORIZED

    def test_get_message_error(self):
        self.client = APIClient(HTTP_AUTHORIZATION="")
        result = self.client.get(reverse("search_logs"))
        expected = {"detail": "Authentication credentials were not provided."}
        assert result.json() == expected
