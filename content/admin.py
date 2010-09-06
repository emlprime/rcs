from django.contrib import admin

from rcs.content.models import HomeText, PerformText, ContactText, VideoText, Video, Instructor, Instrument, LearnText, RehearseText, RecordText

class HomeTextAdmin(admin.ModelAdmin):
    pass
admin.site.register(HomeText, HomeTextAdmin)

class ContactTextAdmin(admin.ModelAdmin):
    pass
admin.site.register(ContactText, ContactTextAdmin)

class VideoTextAdmin(admin.ModelAdmin):
    pass
admin.site.register(VideoText, VideoTextAdmin)

class VideoAdmin(admin.ModelAdmin):
    pass
admin.site.register(Video, VideoAdmin)

class InstructorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Instructor, InstructorAdmin)

class InstrumentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Instrument, InstrumentAdmin)

class LearnTextAdmin(admin.ModelAdmin):
    pass
admin.site.register(LearnText, LearnTextAdmin)


class RecordTextAdmin(admin.ModelAdmin):
    pass
admin.site.register(RecordText, RecordTextAdmin)


class RehearseTextAdmin(admin.ModelAdmin):
    pass
admin.site.register(RehearseText, RehearseTextAdmin)

class PerformTextAdmin(admin.ModelAdmin):
    pass
admin.site.register(PerformText, PerformTextAdmin)
