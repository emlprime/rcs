from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect

from rcs.event.models import Event

# Display views


def current_month(request):
    weeks = Event.get_weeks_for_month("2009-10-02")
    weekdays = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    context = {"weeks": weeks, "weekdays": weekdays}
    response = render_to_response("month.html", RequestContext(request, context))
    return response

