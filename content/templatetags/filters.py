from django import template
 
from calendar import Calendar
import datetime
 
import re
 
register = template.Library()
 
@register.tag(name="get_calendar")
def do_calendar(parser, token):
    syntax_help = "syntax should be \"get_calendar for <month> <year> as <var_name>\""
    # This version uses a regular expression to parse tag contents.
    try:
        # Splitting by None == splitting by spaces.
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires arguments, %s" % (token.contents.split()[0], syntax_help)
    m = re.search(r'for (.*?) (.*?) as (\w+)', arg)
    if not m:
        raise template.TemplateSyntaxError, "%r tag had invalid arguments, %s" % (tag_name, syntax_help)
    
    return GetCalendarNode(*m.groups())
 
class GetCalendarNode(template.Node):
    def __init__(self, month, year, var_name):
        self.year = template.Variable(year)
        self.month = template.Variable(month)
        self.var_name = var_name
        
    def render(self, context):
        mycal = Calendar()
        context[self.var_name] = mycal.monthdatescalendar(int(self.year.resolve(context)), int(self.month.resolve(context)))
        
        return ''





"""
#http://djangosnippets.org/snippets/722/
from django import template
from datetime import datetime

register = template.Library()

@register.filter(name='calendar_table')
def calendar_table(value, arg):
  cal = {}
  dates = value.keys()
  dates.sort()
  for date in value:
    d, m, y = date.day, date.month, date.year
    if y not in cal:
      cal[y] = {}
    if m not in cal[y]:
      cal[y][m] = []
    cal[y][m].append(d)
  result = ''
  
  for y in cal:
    result += "<h2 style=\"clear: left\">%d</h2>" % y
    for m in cal[y]:
      sd = datetime(y, m, 1)
      result += sd.strftime("<div class=\"month\"><h3>%B</h3>")
      result += '<table><thead><tr><th>M</th><th>T</th><th>W</th><th>T</th><th>F</th><th>S</th><th>S</th></tr></thead><tbody><tr>'
      days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][m]
      if m == 2 and y % 4 == 0 and (y % 100 <> 0 or y % 400 == 0):
        days_in_month += 1
      w = sd.weekday()
      for i in range(w):
        result += '<td></td>'
        
      for i in range(days_in_month):
        if i in cal[y][m]:
          s = arg.replace('[Y]', "%.4d" % y).replace('[m]', "%.2d" % m).replace('[d]', "%.2d" % d)
          result += "<td><a href=\"%s\">%d</a></td>" % (s, i + 1)
        else:
          result += "<td>%d</td>" % (i + 1)
        w = (w + 1) % 7
        if w == 0 and i + 1 < days_in_month:
          result += "</tr><tr>"

      for i in range(w,7):
        result += '<td></td>'

      result += '</tr></tbody></table></div>'
  return result
"""
