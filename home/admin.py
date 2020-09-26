from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import *


class NoticeAdmin(ModelAdmin):
    search_fields = ['Role', 'Branch', 'PRN_No']
    list_filter = ['Role', 'Branch', 'Time']


class NoticeContact(ModelAdmin):
    search_fields = ['fname', 'lname']
    list_display = ['fname', 'lname', 'Time']
    list_filter = ['Time']


admin.site.register(Member, NoticeAdmin)

admin.site.register(Contact, NoticeContact)
