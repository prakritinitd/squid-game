from django.db import models

class Event (models.Model):
    name = models.CharField(verbose_name="Event Name",max_length=100)
    start = models.DateTimeField(verbose_name=("Event Starting Time"),)
    end = models.DateTimeField(verbose_name=("Event Starting Time"),)

    def __str__(self):
        return self.name