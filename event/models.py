from django.db import models
from datetime import datetime

class Event(models.Model):
    """ Event class for a calendar
    """

    summary = models.CharField(max_length=255)
    location = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date_start = models.DateField()
    date_end = models.DateField(null=True, blank=True)
    created = models.DateField(auto_now_add=True, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    
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
        [weeks[-1].append(None) for i in range(date.weekday() + 1)]

        for day in cls.get_days_of_month(date_str):
            date = datetime(date.year, date.month, day)
            if date.weekday() == 6 and len(weeks) > 0:
                weeks.append([])
            events = []
            weeks[-1].append((day, events))
            
        # pad the end of the calendar
        [weeks[-1].append(None) for i in range(6-date.weekday())]
        
        return weeks

    @classmethod
    def fill_events(cls, weeks, date_str=None):
        date = datetime.strptime(date_str, "%Y-%m-%d")
        calendar = [[]]
        for week in weeks:
            for events_for_day in week:
                if not events_for_day:
                    calendar[-1].append(None)
                    continue
                day = events_for_day[0]
                date = datetime(date.year, date.month, day)
                
                current_date_str = "%02d-%02d-%02d" % (date.year, date.month, day)

                events = Event.get_events_for_day(current_date_str)
                if date.weekday() == 6 and len(calendar) > 0:
                    calendar.append([])
                calendar[-1].append((day, events))

        return calendar

    def display(self):
        result = "<a href='%s'>%s</a>" % (self.url, self.summary)
        return result

    def __unicode__(self):
        return self.summary
        
    def __str__(self):
        return self.summary
        
