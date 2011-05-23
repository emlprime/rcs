from django.template import RequestContext
from django.shortcuts import render_to_response

from django_calendar import DynamicCalendar

from datetime import date

from rcs.content.models import HomeText, PerformText, ContactText, VideoText, Video, LearnText, Instructor,  RehearseText, RecordText, RecordEquipment, RecordEquipmentType, PartyText

def home(request):
    """Submits the home page information to the URL
    """
    template = "index.html"
    home_text = HomeText.objects.latest()
    context=locals()
    return render_to_response(template, context, context_instance=RequestContext(request))

def party(request):
    """Submits the party page information to the URL
    """
    template = "party.html"
    party_text = PartyText.objects.latest()
    context=locals()
    return render_to_response(template, context, context_instance=RequestContext(request))

def contact(request):
    """Submits the contact page information to the URL
    """
    template = "contact.html"
    contact_text = ContactText.objects.latest()
    context=locals()
    return render_to_response(template, context, context_instance=RequestContext(request))

def perform(request):
    """Submits the perform page information to the URL
    """
    template = "perform.html"
    perform_list = PerformText.objects.all()
    context=locals()
    return render_to_response(template, context, context_instance=RequestContext(request))

def rehearse(request):
    """Submits the rehearse page information to the URL
    """
    template = "rehearse.html"
    rehearse_text = RehearseText.objects.latest()
    context=locals()
    return render_to_response(template, context, context_instance=RequestContext(request))

def record(request):
    """Submits the record page information to the URL
    """
    template = "record.html"
    record_text = RecordText.objects.latest()
    record_equipment = RecordEquipmentType.objects.all()
    context=locals()
    return render_to_response(template, context, context_instance=RequestContext(request))

def learn(request):
    """Submits the learn page information to the URL
    """
    template = "learn.html"
    learn_text = LearnText.objects.latest()
    context=locals()
    return render_to_response(template, context, context_instance=RequestContext(request))

def voice(request):
    """Submits the voice instructors to the URL
    """
    template="instructors.html"
    instructors = Instructor.objects.filter(instrument="V")
    context=locals()
    return render_to_response(template, context, context_instance=RequestContext(request))

def guitar(request):
    """Submits the guitar instructors to the URL
    """
    template="instructors.html"
    instructors = Instructor.objects.filter(instrument="G")
    context=locals()
    return render_to_response(template, context, context_instance=RequestContext(request))

def bass(request):
    """Submits the bass instructors to the URL
    """
    template="instructors.html"
    instructors = Instructor.objects.filter(instrument="B")
    context=locals()
    return render_to_response(template, context, context_instance=RequestContext(request))

def piano(request):
    """Submits the piano instructors to the URL
    """
    template="instructors.html"
    instructors = Instructor.objects.filter(instrument="P")
    context=locals()
    return render_to_response(template, context, context_instance=RequestContext(request))

def drums(request):
    """Submits the drums instructors to the URL
    """
    template="instructors.html"
    instructors = Instructor.objects.filter(instrument="D")
    context=locals()
    return render_to_response(template, context, context_instance=RequestContext(request))

def woodwinds(request):
    """Submits the woodwinds instructors to the URL
    """
    template="instructors.html"
    instructors = Instructor.objects.filter(instrument="W")
    context=locals()
    return render_to_response(template, context, context_instance=RequestContext(request))

def mandolin(request):
    """Submits the mandolin instructors to the URL
    """
    template="instructors.html"
    instructors = Instructor.objects.filter(instrument="M")
    context=locals()
    return render_to_response(template, context, context_instance=RequestContext(request))

def videos(request):
    """Submits the videos page information to the URL
    """
    template = "videos.html"
    video_text = VideoText.objects.latest()
    videos = Video.objects.all()
    context=locals()
    return render_to_response(template, context, context_instance=RequestContext(request))

def calendar(request):
    """Submits the calendar page information to the URL
    """
    template = "calendar.html"
#    foo = "bar"
#    month = date.today().month
#    print month
#    year = date.today().year
#    print year
    c = DynamicCalendar()
    calendar_html = c.generate_calendar()
    context=locals()
    return render_to_response(template, context, context_instance=RequestContext(request))
