from django.contrib.admin import ModelAdmin
from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(ModelAdmin):
    """
    Post model view on django admin.
    """

    list_display = (
        'title',
        'slug',
        'date',
    )
