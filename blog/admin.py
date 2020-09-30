from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import *


class BlogModel(ModelAdmin):
    list_display = ['title', 'time']
    search_fields = ['title', 'time', 'content']
    list_filter = ['time']


admin.site.register(Blog, BlogModel)
admin.site.register(Like)
