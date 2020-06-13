from django.db import models


class Log(models.Model):
    log = models.CharField(max_length=200, blank=False, null=False)
    level = models.CharField(max_length=20, blank=False, null=False)
    event = models.IntegerField(blank=False, null=False)
    archived = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def archived_true(self):
        self.archived = True

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.log
