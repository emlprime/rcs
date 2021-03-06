from django.conf.urls.defaults import *

from rcs.settings import MEDIA_ROOT

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^site_media/(.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
    (r'^admin/(.*)$', admin.site.root),
    (r'^calendar/', include('rcs.event.urls'))

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

)

urlpatterns += patterns('rcs.content.views',
     (r'^$', "home"),
     (r'^learn/$', "learn"),
     (r'^learn/individual/about/$', "learn"),
     (r'^learn/individual/voice/$', "voice"),
     (r'^learn/individual/guitar/$', "guitar"),
     (r'^learn/individual/bass/$', "bass"),
     (r'^learn/individual/piano/$', "piano"),
     (r'^learn/individual/drums/$', "drums"),
     (r'^learn/individual/woodwinds/$', "woodwinds"),
     (r'^learn/individual/mandolin/$', "mandolin"),
     (r'^rehearse/$', "rehearse"),
     (r'^record/$', "record"),
     (r'^perform/$', "perform"),
     (r'^contact/$', "contact"),
     (r'^videos/$', "videos"),
     (r'^party/$', "party"),
)
