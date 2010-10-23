from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext, loader
from django.template.loader import render_to_string

from django_calendar import DynamicCalendar

import os
import datetime
   

# over-ride this by a custom path to your required media in your HTML head
def calendar_js(request, name):

    path = os.path.join(os.path.dirname(__file__), 'templates')
    js_template = '%s/%s' % (path,name)

    template_files = (
        js_template,
    )
    
    t = loader.select_template(template_files)
    
    context = RequestContext(request)

    return HttpResponse(t.render(context), content_type="application/x-javascript")
    
        
    
# over-ride this by a custom path to your required media in your HTML head
def calendar_css(request, name):

    path = os.path.join(os.path.dirname(__file__), 'templates')
    js_template = '%s/%s' % (path,name)

    template_files = (
        js_template,
    )
    
    t = loader.select_template(template_files)
    
    context = RequestContext(request)

    return HttpResponse(t.render(context), content_type="text/css")



def date_html(request, startday=None, startmonth=None, startyear=None):
    " return a list of date objects within the given range "
    
    # use excepted date format, not english
    c = DynamicCalendar(year=startyear, month=startmonth, day=startday)
    calendar_html = c.generate_calendar()

    return HttpResponse(calendar_html, mimetype="text/html")


def next(request, startyear=None, startmonth=None, startday=None):
    
    c = DynamicCalendar(year=startyear, month=startmonth, day=startday)
    calendar_html = c.generate_calendar()
    
    return HttpResponse(calendar_html, mimetype="text/html")


# over-ride this by making AJAX non-default
def date_range(request, startyear=None, startmonth=None, startday=None,
                        finishyear=None, finishmonth=None, finishday=None):
    " return a list of date objects within the given range "
    c = DynamicCalendar()
    calendar_html = c.generate_calendar()

    if startyear and finishyear is not None:
        try:
            currentdate = datetime.date(int(startyear),int(startmonth),int(startday))
            enddate = datetime.date(int(finishyear),int(finishmonth),int(finishday))
        except TypeError:
            # non integer passed
            pass
        else:
            date_range = c.range(start = currentdate, finish = enddate)

    elif startyear is not None:
        # single day being looked at
        try:
            currentdate = datetime.date(int(startyear),int(startmonth),int(startday))
        except TypeError:
            # non integer passed
            pass
        else:
            date_range = []
            date_range.append(currentdate)
            
    html =  render_to_string('dates.html', locals())
    
    return HttpResponse(html, mimetype="text/html")

    
