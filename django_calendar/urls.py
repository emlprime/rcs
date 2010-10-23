from django.conf.urls.defaults import *

from django_calendar.views import calendar_js, calendar_css, date_range, date_html

urlpatterns = patterns('django_calendar.views',
    # static media
    url(r'^js/(?P<name>.+)$', 'calendar_js'),
    url(r'^css/(?P<name>.+)$', 'calendar_css'),
    url(r'^(?P<startday>\d{1,2})/(?P<startmonth>\d{1,2})/(?P<startyear>\d{4})/more/$', 'next'),
    url(r'^update/(?P<startday>\d{1,2})/(?P<startmonth>\d{1,2})/(?P<startyear>\d{4})/$', 'date_html'),
    # date navigation
    url(r'^(?P<startyear>\d{4})/(?P<startmonth>\d{1,2})/(?P<startday>\d{1,2})/calendar/(?P<finishyear>\d{4})/(?P<finishmonth>\d{1,2})/(?P<finishday>\d{1,2})/$', 
        'date_range'),
    url(r'^(?P<startyear>\d{4})/(?P<startmonth>\d{1,2})/(?P<startday>\d{1,2})/$', 'date_range'),

)
