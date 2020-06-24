from core.models import Log
from django.test import TestCase


class LogModelTest(TestCase):
    def setUp(self):
        self.log = Log.objects.create(log="Teste1", level="warning1", event=100)
        Log.objects.create(log="Teste2", level="warning2", event=100)
        Log.objects.create(log="Teste3", level="warning3", event=100)
        self.logs = Log.objects.all()

    def test_set_archived_for_true(self):
        self.log.archived_true()
        assert self.log.archived is True

    def test_str_of_log(self):
        exepect = self.log.__str__()
        assert exepect == "Teste1"

    def test_log_equal_one(self):
        expect = self.logs.count()
        assert expect == 3
