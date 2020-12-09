from django.contrib import admin
from django import forms
from .models import RecordModel
'''
class RecordInLine(admin.TabularInline):
    model = RecordModel

class RecordAdmin(admin.ModelAdmin):
    inlines = [RecordInLine]
'''
admin.site.register(RecordModel)