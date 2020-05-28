from core.models import Log
import pytest


@pytest.mark.django_db
def create_one_log():
    log = Log.objects.create(log="Teste")
    return log is True


@pytest.mark.django_db
def test_str_of_log():
    log = Log.objects.create(log="Teste")
    assert log.__str__() == "Teste"


@pytest.mark.django_db
def test_len_of_log_equal_one():
    log = Log.objects.create(log="Teste")
    return log == 1
