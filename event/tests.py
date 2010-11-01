from rcs.event.models import Event

__test__ = {"Event": """
Get relevant data from an event object

>>> print Event.get_events_for_day("2010-10-01")
[]
>>> details = {"date_start": "2010-10-01", "date_end": "2010-10-01", "summary": "SUMMARY", "description": "DESCRIPTION", "location": "LOCATION", "url": "http://www.rcs.com", "created": "2010-10-01"}
>>> event = Event.objects.create(**details)
>>> events = Event.get_events_for_day("2010-10-01")
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
>>> weeks = Event.get_weeks_for_month("2009-10-02")
>>> print weeks
[[None, None, None, None, None, (1, []), (2, []), (3, [])], [(4, []), (5, []), (6, []), (7, []), (8, []), (9, []), (10, [])], [(11, []), (12, []), (13, []), (14, []), (15, []), (16, []), (17, [])], [(18, []), (19, []), (20, []), (21, []), (22, []), (23, []), (24, [])], [(25, []), (26, []), (27, []), (28, []), (29, []), (30, []), (31, [])]]
>>> details = {"date_start": "2009-10-02", "date_end": "2009-10-02", "summary": "Stuff", "description": "DESCRIPTION 3", "location": "LOCATION", "url": "http://www.rcs.com", "created": "2009-10-02"}
>>> event = Event.objects.create(**details)
>>> details = {"date_start": "2009-10-02", "date_end": "2009-10-02", "summary": "Things", "description": "DESCRIPTION 3", "location": "LOCATION", "url": "http://www.rcs.com", "created": "2009-10-02"}
>>> event = Event.objects.create(**details)
>>> details = {"date_start": "2009-10-03", "date_end": "2009-10-03", "summary": "Other Things", "description": "DESCRIPTION 3", "location": "LOCATION", "url": "http://www.rcs.com", "created": "2009-10-03"}
>>> event = Event.objects.create(**details)
>>> calendar = Event.fill_events(weeks, "2009-10-02")
>>> print calendar
[[None, None, None, None, None, (1, []), (2, [<Event: Stuff>, <Event: Things>]), (3, [<Event: Other Things>])], [(4, []), (5, []), (6, []), (7, []), (8, []), (9, []), (10, [])], [(11, []), (12, []), (13, []), (14, []), (15, []), (16, []), (17, [])], [(18, []), (19, []), (20, []), (21, []), (22, []), (23, []), (24, [])], [(25, []), (26, []), (27, []), (28, []), (29, []), (30, []), (31, [])]]
>>> print event.display()
<a href='http://www.rcs.com'>Other Things</a>
>>> print Event.get_next_month("2009-10-03")
2009-11-01 00:00:00
>>> print Event.next_month_url("2009-10-03")
/calendar/2009/11/
>>> print Event.get_previous_month("2009-10-03")
2009-09-01 00:00:00
>>> print Event.previous_month_url("2009-10-03")
/calendar/2009/09/
>>> print event.get_next_month("2010-01-04")
2010-02-01 00:00:00
>>> print event.next_month_url("2010-01-04")
/calendar/2010/02/
>>> print event.get_previous_month("2010-01-04")
2009-12-01 00:00:00
>>> print event.previous_month_url("2010-01-04")
/calendar/2009/12/
"""}

