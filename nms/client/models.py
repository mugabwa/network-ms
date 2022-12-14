from django.db import models
from django.utils import timezone


class Clients(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    location = models.CharField(max_length=100)
    contacts = models.CharField(max_length=20)
    status = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    custom_unique_feild = models.CharField(max_length=250, unique=True)

    def save(self, *args, **kwargs):
        self.custom_unique_feild = (
            self.first_name+'/'+self.last_name+'/'+self.location)
        self.custom_unique_feild = self.custom_unique_feild.replace(' ', '_')
        self.custom_unique_feild = self.custom_unique_feild.lower()
        super(Clients, self).save(*args, **kwargs)
