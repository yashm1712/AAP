from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import *


class WebinarModel(ModelAdmin):
    list_display = ['Title', 'Date']
    search_fields = ['Title', 'Memo']
    list_filter = ['Date']


admin.site.register(Webinar, WebinarModel)


class DoubtModel(ModelAdmin):
    list_display = ['Question', 'Time']
    search_fields = ['Time']
    list_filter = ['Time']


admin.site.register(Doubt, DoubtModel)
admin.site.register(Answer)


class ReunionModel(ModelAdmin):
    list_display = ['Title', 'Date', 'Place']
    search_fields = ['Title']
    list_filter = ['Date']


admin.site.register(Reunion, ReunionModel)

admin.site.register(Achievement)
