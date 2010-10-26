from django.db import models

class Event(models.Model):
    """ Event class for a calendar
    """

    summary = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    created = models.DateTimeField()
    url = models.URLField()
    
    @classmethod
    def get_events_for_day(cls, date=None):
        events = cls.objects.filter(date_start=date)
        return events


