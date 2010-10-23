from django import template
register = template.Library()

def calendar_media():
    
    media_string = '<script type="text/javascript" src="/calendar/js/jquery.color.js"></script>\n \
					<script type="text/javascript" src="/calendar/js/calendar.js"></script>\n \
                    <link rel="stylesheet" type="text/css" href="/calendar/css/calendar.css" media="screen" />'
    return media_string

register.simple_tag(calendar_media)

