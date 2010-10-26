from rcs.event.models import Event

__test__ = {"Event": """
Get relevant data from an event object

>>> print Event.get_events_for_day("2010-10-01")
[]
>>> details = {"date_start": "2010-10-01", "date_end": "2010-10-01", "summary": "SUMMARY", "description": "DESCRIPTION", "location": "LOCATION", "url": "http://www.rcs.com", "created": "2010-10-01"}
>>> event = Event.objects.create(**details)
>>> events = event.get_events_for_day("2010-10-01")
>>> print len(events)
1
>>> details = {"date_start": "2010-10-02", "date_end": "2010-10-02", "summary": "SUMMARY 2", "description": "DESCRIPTION 2", "location": "LOCATION", "url": "http://www.rcs.com", "created": "2010-10-02"}
>>> event = Event.objects.create(**details)
>>> events = event.get_events_for_day("2010-10-02")
>>> print len(events)
1
>>> details = {"date_start": "2010-10-02", "date_end": "2010-10-02", "summary": "SUMMARY 3", "description": "DESCRIPTION 3", "location": "LOCATION", "url": "http://www.rcs.com", "created": "2010-10-02"}
>>> event = Event.objects.create(**details)
>>> events = event.get_events_for_day("2010-10-02")
>>> print len(events)
2
>>> print Event.get_days_of_month("2010-01-02")
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
>>> print Event.get_days_of_month("2010-02-02")
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
>>> print Event.get_days_of_month("2010-03-02")
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
>>> print Event.get_days_of_month("2010-04-02")
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
>>> print Event.get_days_of_month("2010-05-02")
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
>>> print Event.get_days_of_month("2010-06-02")
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
>>> print Event.get_days_of_month("2010-07-02")
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
>>> print Event.get_days_of_month("2010-08-02")
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
>>> print Event.get_days_of_month("2010-09-02")
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
>>> print Event.get_days_of_month("2010-10-02")
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
>>> print Event.get_days_of_month("2010-12-02")
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

"""}

