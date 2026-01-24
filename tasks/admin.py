from django.contrib import admin
from django.utils.html import format_html

from .models import Task, Attechment, SubTask, Category


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'colored_slug', 'display_description', 'display_image')

    @admin.display(description='Description')
    def display_description(self, obj):
        return f'{obj.description}'[:50]
    
    @admin.display(description='Colored Slug')
    def colored_slug(self, obj):
        return format_html(
            '<span style="color: red;">{}</span>',
            obj.slug
        )
    
    @admin.display(description='Image')
    def display_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 4px;">',
                obj.image.url
            )
        else:
            return '-'


@admin.register(Task)
class TaskModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
