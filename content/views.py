from django.template import RequestContext
from django.shortcuts import render_to_response

from rcs.content.models import HomeText, PerformText, ContactText, VideoText, Video, LearnText, Instructor, Instrument,  RehearseText, RecordText, RecordEquipment, RecordEquipmentType

def home(request):
    """Submits the home page information to the URL
    """
    template = "index.html"
    home_text = HomeText.objects.latest()
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
    print rehearse_text
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
    instruments = Instrument.objects.all()
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
    context=locals()
    return render_to_response(template, context, context_instance=RequestContext(request))
