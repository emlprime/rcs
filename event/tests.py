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
"""}

