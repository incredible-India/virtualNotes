from django.contrib import admin

from . import models
# Register your models here.
@admin.register(models.StickyNotes)
class StickyNotesAdmin(admin.ModelAdmin):
    list_display = ['id','textIs','dateOf','userid']
# Register your models here.
#for the categories
@admin.register(models.Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['id','name','dateOf','cimg','uid',]