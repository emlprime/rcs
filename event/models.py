from django.db import models
from datetime import datetime

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

    @classmethod
    def get_days_of_month(cls, date_str=None):
        date = datetime.strptime(date_str, "%Y-%m-%d")
        
        # 30 days hath september, april, june and november
        # all the rest have 31
        end = 30 if date.month in [4,6,9,11] else 31
        # except for little February
        if date.month == 2:
            end = 28

        return range(1, end + 1)

    @classmethod
    def get_weeks_for_month(cls, date_str=None):
        date = datetime.strptime(date_str, "%Y-%m-%d")
        weeks = [[]]
        # pad the front of the calendar
        [weeks[-1].append(None) for i in range(date.weekday()-1)]

        for day in cls.get_days_of_month(date_str):
            date = datetime(date.year, date.month, day)
            if date.weekday() == 0 and len(weeks) > 0:
                weeks.append([])
            events = []
            weeks[-1].append((day, events))
            
        # pad the end of the calendar
        [weeks[-1].append(None) for i in range(6-date.weekday())]
        
        return weeks


