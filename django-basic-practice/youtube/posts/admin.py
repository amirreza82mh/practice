from django.contrib import admin
from . import models

class CommentAdminInline(admin.TabularInline):
    model = models.Comment
    fields = ['text', ]
    extra = 0

@admin.register(models.Post)
class AdminPost(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'is_enable',
        'create_time',
        'update_time'
    ]

    inlines = [CommentAdminInline, ]

# admin.site.register(models.Post, AdminPost)

# class AdminComment(admin.ModelAdmin):
#     list_display = [
#         'id',
#         'post',
#         'create_time'
#     ]

# admin.site.register(models.Comment, AdminComment)
