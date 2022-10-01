from django.contrib import admin

from post import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'updated_at')
    list_filter = ('title',)
    search_fields = ('description',)
    list_display_links = ('title',)
    empty_value_display = '-пусто-'


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'message', 'created_at', 'updated_at')
    list_filter = ('post',)
    search_fields = ('message',)
    list_display_links = ('post',)
    empty_value_display = '-пусто-'
