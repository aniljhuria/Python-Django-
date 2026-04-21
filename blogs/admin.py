from django.contrib import admin
from .models import Category,Blog,Comment

# from django.contrib import admin
# from django.contrib.sessions.models import Session
# from django.contrib.contenttypes.models import ContentType
# from django.contrib.admin.models import LogEntry

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    #prepopulated_fields={'slug':('title',)}
    readonly_fields = ('slug',)
    list_display=('title','category','auther','status','is_featured')
    search_fields=('id','title','category__category_name','status')
    list_editable=('is_featured','status')


class CommentAdmin(admin.ModelAdmin):    
    list_display=('comment','blog','user','created_at')
   


admin.site.register(Category)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Comment,CommentAdmin)


# Session
# @admin.register(Session)
# class SessionAdmin(admin.ModelAdmin):
#     list_display = ('session_key', 'expire_date')


# ContentType
# @admin.register(ContentType)
# class ContentTypeAdmin(admin.ModelAdmin):
#     list_display = ('app_label', 'model')


# LogEntry
# @admin.register(LogEntry)
# class LogEntryAdmin(admin.ModelAdmin):
#     list_display = ('user', 'content_type', 'action_flag', 'action_time')