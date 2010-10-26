from django.conf.urls.defaults import *

from event.views import current_month

urlpatterns = patterns('event.views',
    url(r'^$', 'current_month'),
)
