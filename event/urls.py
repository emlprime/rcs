from django.conf.urls.defaults import *

from event.views import month_calendar

urlpatterns = patterns('event.views',
    url(r'^$', 'month_calendar'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$', 'month_calendar'),
)
