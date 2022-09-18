from datetime import timedelta
from django.db import models
from django.utils import timezone

from nms.client.models import Clients


class Bandwidth(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    package = models.CharField(max_length=5)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField()
    valid = models.BooleanField(default=False)

    def _end_date(self):
        self.end_date = self.start_date + timedelta(days=30)
        if self.end_date < timezone.now():
            self.valid = False
        else:
            self.valid = True

    def save(self, *args, **kwargs):
        self._end_date()
        super(Bandwidth, self).save(*args, **kwargs)
