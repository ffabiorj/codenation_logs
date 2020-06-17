from core.models import Log
import pytest


@pytest.mark.django_db
def test_set_archived_for_true():
    log = Log.objects.create(log="Teste", level="warning", event=100)
    log.archived_true()
    assert log.archived is True


@pytest.mark.django_db
def test_str_of_log():
    log = Log.objects.create(log="Teste", level="warning", event=100)
    assert log.__str__() == "Teste"


@pytest.mark.django_db
def test_len_of_log_equal_one():
    log = Log.objects.create(log="Teste", level="warning", event=100)
    return log == 1
