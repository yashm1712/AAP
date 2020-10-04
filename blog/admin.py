from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import *


class BlogModel(ModelAdmin):
    list_display = ['title', 'time']
    search_fields = ['title', 'time', 'content']
    list_filter = ['time']


class BlogComment(ModelAdmin):
    list_display = ['comments', 'timestamp']
    list_filter = ['timestamp']


admin.site.register(Blog, BlogModel)
admin.site.register(Comment, BlogComment)

# admin.site.register(Like)
