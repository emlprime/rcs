*** My First Ever Proper Django App *

DEPENDENCIES:

  JavaScript
  JQuery, basic

"django-calendar"

After adding to settings.py;

(i) load the required custom template tags from your base template
    {% load calendar_tags %}

(ii) render the calendar's media requests in the <head> of your base template BELOW your jquery request, and do so with the following template tag:
    {% calendar_media %}

(iii) Include the url.conf from the base conf
    (r'^calendar/', include('html_calendar.urls')),

(iv) Import me into your view...
    from django_calendar import DynamicCalendar

(v) Create it and the HTML in said view:

    c = DynamicCalendar()
    calendar_html = c.generate_calendar()

(vi) Include calendar in the rendered HTML template
    {{calendar_html|safe}}
    
(vii) For the time being, to over-ride the default AJAX behaviour, you can set do_with_ajax as false in the extrahead block, e.g.:

    {% block extrahead %}
    <script type="text/javascript">
    var do_with_ajax = false
    </script>
    {% endblock%}
    
    Do this after the django-calendar media calls and your free to over-ride the regex's in the url conf for your own app.


That should be it. I'll deliver date objects over the selected range for you to work with. See my Django-GanttChart app for an example.

Please feedback, make use of + let me know what you do with it. I'll link to your page from my site if you let me know.

thanks

Simon,
noisyboiler@googlemail.com