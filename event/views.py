from datetime import datetime

from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect

from rcs.event.models import Event


def month_calendar(request, year=None, month=None):
    if not year or not month:
        current_time = datetime.now()
        date_str = current_time.strftime("%Y-%m-%d")
    else:
        date_str = "%s-%s-01" % (year, month)
        
    weeks = Event.get_weeks_for_month(date_str)
    calendar = Event.fill_events(weeks, date_str)

    weekdays = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    context = {"calendar": calendar, "weekdays": weekdays}
    response = render_to_response("month.html", RequestContext(request, context))
    return response

