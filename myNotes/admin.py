from django.contrib import admin

from . import models
# Register your models here.
@admin.register(models.StickyNotes)
class StickyNotesAdmin(admin.ModelAdmin):
    list_display = ['id','textIs','dateOf','userid']
# Register your models here.
