from django.db import models
from django.utils.timezone import now


class Log(models.Model):
    log = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)
        
    def __str__(self):
        return self.log