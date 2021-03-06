from django.db import models
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

DATE_FORMAT = "%Y-%m-%d"

class Event(models.Model):
    """ Event class for a calendar
    """

    summary = models.CharField(max_length=255)
    location = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date_start = models.DateTimeField()
    created = models.DateField(auto_now_add=True, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    
    @classmethod
    def get_events_for_day(cls, date=None):
        today = datetime.strptime(date, DATE_FORMAT)
        next_date = today + timedelta(days=1)
        events = cls.objects.filter(date_start__gte=date, date_start__lt=next_date)
        return events

    @classmethod
    def get_days_of_month(cls, date_str=None):
        date = datetime.strptime(date_str, DATE_FORMAT)
        
        # 30 days hath september, april, june and november
        # all the rest have 31
        end = 30 if date.month in [4,6,9,11] else 31
        # except for little February
        if date.month == 2:
            end = 28

        return range(1, end + 1)

    @classmethod
    def get_weeks_for_month(cls, date_str=None):
        date = datetime.strptime(date_str, DATE_FORMAT)
        weeks = [[]]
        # pad the front of the calendar
        if date.weekday() != 6:
            [weeks[-1].append(None) for i in range(date.weekday() + 1)]

        for day in cls.get_days_of_month(date_str):
            date = datetime(date.year, date.month, day)
            if date.weekday() == 6 and len(weeks) > 0:
                weeks.append([])
            events = []
            weeks[-1].append((day, events))
            
        # pad the end of the calendar
        last_week_length = len(weeks[-1])
        total_week_length = 7
        days_to_pad = total_week_length - last_week_length
        [weeks[-1].append(None) for i in range(days_to_pad)]
        #raise "Error"
        
        return weeks

    @classmethod
    def fill_events(cls, weeks, date_str=None):
        date = datetime.strptime(date_str, DATE_FORMAT)
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

    @classmethod
    def get_previous_month(cls, date_str):
        current_date = datetime.strptime(date_str, DATE_FORMAT)
        next_month = current_date + relativedelta(months=-1, day=1)
        return next_month

    @classmethod
    def get_next_month(cls, date_str):
        current_date = datetime.strptime(date_str, DATE_FORMAT)
        next_month = current_date + relativedelta(months=+1, day=1)
        return next_month

    @classmethod
    def next_month_url(cls, date_str):
        next_month = Event.get_next_month(date_str)
        year = next_month.year
        month = next_month.month
        return "/calendar/%d/%02d/" % (year, month)

    @classmethod
    def previous_month_url(cls, date_str):
        previous_month = Event.get_previous_month(date_str)
        year = previous_month.year
        month = previous_month.month
        return "/calendar/%d/%02d/" % (year, month)

    @classmethod
    def get_events_from_calendar(cls, calendar):
        # return a list of events for a calendar
        return [day[1][0] for week in calendar for day in week if day and len(day[1]) > 0]


    def display(self):
        result = "<a href='%s' class='event_link' title=\"%s\">%s</a>" % (self.url, self.display_tooltip(), str(self))
        return result

    def display_tooltip(self):
        return "<title>%s</title><p>%s</p>" % (self.summary, self.description)

    def __unicode__(self):
        return self.summary
        
    def __str__(self):
        summary = self.summary 
        a = self.date_start
        time = "%d:%d %s" % (a.hour, a.minute, a.strftime("%p"))
        return "%s<br />%s<br />" % (summary, time)
        
