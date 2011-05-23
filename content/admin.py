from django.contrib import admin

from rcs.content.models import HomeText, PerformText, ContactText, VideoText, Video, Instructor, LearnText, RehearseText, RecordText, RecordEquipment, RecordEquipmentType, PartyText

class HomeTextAdmin(admin.ModelAdmin):
    pass
admin.site.register(HomeText, HomeTextAdmin)

class PartyTextAdmin(admin.ModelAdmin):
    pass
admin.site.register(PartyText, PartyTextAdmin)

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

class LearnTextAdmin(admin.ModelAdmin):
    pass
admin.site.register(LearnText, LearnTextAdmin)

class RecordTextAdmin(admin.ModelAdmin):
    pass
admin.site.register(RecordText, RecordTextAdmin)

class RecordEquipmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(RecordEquipment, RecordEquipmentAdmin)

class RecordEquipmentTypeAdmin(admin.ModelAdmin):
    pass
admin.site.register(RecordEquipmentType, RecordEquipmentTypeAdmin)

class RehearseTextAdmin(admin.ModelAdmin):
    pass
admin.site.register(RehearseText, RehearseTextAdmin)

class PerformTextAdmin(admin.ModelAdmin):
    pass
admin.site.register(PerformText, PerformTextAdmin)
