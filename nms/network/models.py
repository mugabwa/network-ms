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
    terminated = models.BooleanField(default=False)
    termination_date = models.DateTimeField(null=True)
    untermination_date = models.DateTimeField(null=True)

    def setValid(self):
        acceptable_time = (self.start_date <= timezone.now()+timedelta(hours=1) and
            self.end_date >= timezone.now())
        if ( acceptable_time and not self.terminated):
            self.valid = True
        else:
            self.valid = False

    def _end_date(self):
        self.end_date = self.start_date + timedelta(days=30)
        self.setValid()
    
    def create(self, *args, **kwargs):
        self._end_date()
        super(Bandwidth, self).create(*args, **kwargs)

    def __str__(self):
        output = str(self.client) + ' ' + self.package + ' {}'
        return output.format('Valid' if self.valid else 'Not Valid')

