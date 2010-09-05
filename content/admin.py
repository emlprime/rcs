from django.contrib import admin

from rcs.content.models import HomeText, PerformText, ContactText
# LearnText, RecordText, RehearseText,

class HomeTextAdmin(admin.ModelAdmin):
    pass
admin.site.register(HomeText, HomeTextAdmin)

class ContactTextAdmin(admin.ModelAdmin):
    pass
admin.site.register(ContactText, ContactTextAdmin)

"""
class LearnTextAdmin(admin.ModelAdmin):
    pass
admin.site.register(LearnText, LearnTextAdmin)

class RecordTextAdmin(admin.ModelAdmin):
    pass
admin.site.register(RecordText, RecordTextAdmin)

class RehearseTextAdmin(admin.ModelAdmin):
    pass
admin.site.register(RehearseText, RehearseTextAdmin)
"""
class PerformTextAdmin(admin.ModelAdmin):
    pass
admin.site.register(PerformText, PerformTextAdmin)
