"""
Copyright (c) 2009, Simon Harrison.

All rights reserved.

    This file is part of django-calendar.

    django-calendar is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    django-calendar is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with django-calendar.  If not, see <http://www.gnu.org/licenses/>.
"""

from django.template.loader import render_to_string
from django.template import RequestContext, loader
from django.http import HttpResponse, Http404, HttpResponseRedirect

import re, datetime, calendar
from datetime import timedelta

    
class DynamicCalendar:
    " An HTML calendar class "
    
    def __init__(self, year=None, month=None, day=None):
        " initialises an html calendar based on the current date "
        if year is not None:
            self.today = datetime.date(year=int(year), month=int(month), day=int(day))
        else:
            self.today = datetime.date.today()
        
        self.current = re.split('-', str(self.today))
        self.current_month_as_number = int(self.current[1])
        self.current_day = int(re.sub('\A0', '', self.current[2]))
        self.current_year = int(self.current[0])    
        # returns the month as a list of integers representing the days
        self.weeks = calendar.monthcalendar(self.current_year, self.current_month_as_number)
        # grab the final day of the month
        self.last = max(self.weeks[-1:][0])
        
    def generate_calendar(self, start_day=0):
        " render the HTML for the calendar "
        return render_to_string('calendar.html', {
            'self' : self,
            'month' : self.today.month,
            'current_day' : self.current_day,
            'current_year' : self.current_year,
            'current_month' : self.current_month_as_number,
            'last' : self.last,
        })
        
    def current_month(self):
        " returns the currently viewed month as an integer "
        return self.current_month_as_number
    
    def next_month(self):
        " returns the next month as an integer "
        mo = self.current_month_as_number
        if mo == 12:
            return 1
        else:
            return mo + 1
        
    def month_next(self):
        " returns a URL for the month following the users current month "
        yr, mo = divmod(self.current_year * 12 + self.current_month_as_number, 12)
        d = datetime.date(yr, mo + 1, 1)
        mo = int(re.split('-', str(d))[1])
        return '/calendar/%d/%s/%s/' % (self.current_day, mo, self.current_year)
        
    def month_previous(self):
        " returns a URL for the month preceding the users current month "
        yr, mo = divmod(self.current_year * 12 + self.current_month_as_number - 1, 12)
        if mo == 0: mo = 12
        d = datetime.date(yr, mo, 1)
        mo = int(re.split('-', str(d))[1])
        return '/calendar/%s/%s/%s/' % (self.current_day, mo, self.current_year)
    
    def year_next(self):
        " returns a URL for the month following the users current month "
        return '/calendar/%s/%s/%s/' % (self.current_day, self.current_month_as_number, self.current_year+1)
        
    def year_previous(self):
        " returns a URL for the month preceding the users current month "
        return '/calendar/%s/%s/%s/' % (self.current_day, self.current_month_as_number, self.current_year-1)

    # check if arguments are date objects!
    def range(self, start=None, finish=None):
        " returns the dates selected on the calendat interface as a list "
        date_range = []
        while start <= finish: 
           date_range.append(start)
           start += datetime.timedelta(days=1)  
        return date_range
    
