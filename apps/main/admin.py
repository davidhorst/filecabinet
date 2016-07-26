from django.contrib import admin

# Register your models here.
from .models import Icon, Color, Property, Event, Note, File, Alert

class IconAdmin(admin.ModelAdmin):
	pass
admin.site.register(Icon, IconAdmin)

class ColorAdmin(admin.ModelAdmin):
	pass
admin.site.register(Color, ColorAdmin)

class PropertyAdmin(admin.ModelAdmin):
	pass
admin.site.register(Property, PropertyAdmin)

class EventAdmin(admin.ModelAdmin):
	pass
admin.site.register(Event, EventAdmin)

class NoteAdmin(admin.ModelAdmin):
	pass
admin.site.register(Note, NoteAdmin)

class FileAdmin(admin.ModelAdmin):
	pass
admin.site.register(File, FileAdmin)

class AlertAdmin(admin.ModelAdmin):
	pass
admin.site.register(Alert, AlertAdmin)