from django.db import models
from django.utils import timezone


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField('Your description goes here!')
    date_created = models.DateTimeField(default=timezone.now())
    expiry_date = models.DateTimeField(default=timezone.now() + timezone.timedelta(weeks=1))

    def __str__(self):
        return self.title
