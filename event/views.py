from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect

from rcs.event.models import Event

# Display views


def current_month(request):
    context = {}
    response = render_to_response("month.html", RequestContext(request, context))
    return response

